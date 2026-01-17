import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
DATA_PATH = "../../data/processed/energy_panel_clean.csv"
OUTPUT_PLOT = "../../figures/depletion_forecast/depletion_risk_index.png"

RESOURCES = ["Oil", "Gas", "Coal"]
START_YEAR = 1990
END_YEAR = 2022

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

df = df[
    (df["resource"].isin(RESOURCES)) &
    (df["metric"].isin(["Consumption", "Production"])) &
    (df["year"].between(START_YEAR, END_YEAR))
]

# =========================
# AGGREGATE BY REGION
# =========================
df_regional = (
    df.groupby(["region", "resource", "metric", "year"])["value"]
    .sum()
    .reset_index()
)

# =========================
# CAGR FUNCTION
# =========================
def cagr(series):
    if len(series) < 2:
        return np.nan
    start, end = series.iloc[0], series.iloc[-1]
    if start <= 0 or end <= 0:
        return np.nan
    years = len(series) - 1
    return (end / start) ** (1 / years) - 1

# =========================
# CALCULATE TRENDS
# =========================
results = []

for (region, resource, metric), g in df_regional.groupby(
    ["region", "resource", "metric"]
):
    g = g.sort_values("year")
    growth = cagr(g["value"])
    results.append([region, resource, metric, growth])

df_trends = pd.DataFrame(
    results,
    columns=["region", "resource", "metric", "growth"]
)

# =========================
# DEPLETION RISK INDEX
# =========================
pivot = df_trends.pivot_table(
    index=["region", "resource"],
    columns="metric",
    values="growth"
).reset_index()

pivot["depletion_risk_index"] = (
    pivot["Consumption"] - pivot["Production"]
)

pivot = pivot.dropna(subset=["depletion_risk_index"])

# =========================
# OUTPUT TABLE
# =========================
print("\n=== Depletion Risk Index (top risk) ===")
print(
    pivot.sort_values("depletion_risk_index", ascending=False)
    .head(10)
)

# =========================
# VISUALIZATION
# =========================
plt.figure(figsize=(12,6))

for resource in RESOURCES:
    subset = pivot[pivot["resource"] == resource]
    plt.bar(
        subset["region"],
        subset["depletion_risk_index"],
        label=resource
    )

plt.axhline(0, color="black", linewidth=1)
plt.ylabel("Depletion Risk Index")
plt.title("Resource Depletion Risk by Region\n(Consumption growth – Production growth)")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_PLOT, dpi=300)
plt.show()
