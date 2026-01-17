import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Настройки графиков
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Папка для сохранения графиков
output_dir = "../../figures/data_visualization"
os.makedirs(output_dir, exist_ok=True)

# Загрузка очищенного датасета
df = pd.read_csv("../../data/processed/energy_panel_clean.csv")

# Фильтруем по интересующим ресурсам и метрикам
resources = ["Oil", "Gas", "Coal", "Electricity", "Energy", "CO2"]
metrics = ["Consumption", "Production", "Emissions", "Reserves"]

df_vis = df[df["resource"].isin(resources) & df["metric"].isin(metrics)].copy()

# =========================
# 1. Гистограммы
# =========================
for res in resources:
    for met in metrics:
        sub = df_vis[(df_vis["resource"] == res) & (df_vis["metric"] == met)]
        if sub.empty:
            continue
        plt.figure()
        sns.histplot(sub["value"], bins=30, kde=True)
        plt.title(f"{met} of {res} – distribution")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, f"hist_{res}_{met}.png"))
        plt.close()

# =========================
# 2. Boxplot
# =========================
plt.figure()
sns.boxplot(data=df_vis, x="resource", y="value", hue="metric")
plt.title("Boxplot of resources by metric")
plt.yscale("log")
plt.savefig(os.path.join(output_dir, "boxplot_resources_metrics.png"))
plt.close()

# =========================
# 3. Violin plot по регионам
# =========================
plt.figure()
sns.violinplot(data=df_vis[df_vis["region"].notna()],
               x="region", y="value", hue="resource", split=True)
plt.xticks(rotation=90)
plt.title("Distribution of resources by region")
plt.yscale("log")
plt.savefig(os.path.join(output_dir, "violin_by_region.png"))
plt.close()

# =========================
# 4. Scatter plot: Production vs Consumption
# =========================
prod = df_vis[df_vis["metric"] == "Production"]
cons = df_vis[df_vis["metric"] == "Consumption"]
merge_pc = prod.merge(cons, on=["country", "year", "resource"], suffixes=("_prod", "_cons"))

plt.figure()
sns.scatterplot(data=merge_pc, x="value_cons", y="value_prod", hue="resource", alpha=0.7)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Consumption")
plt.ylabel("Production")
plt.title("Production vs Consumption by resource")
plt.savefig(os.path.join(output_dir, "scatter_prod_vs_cons.png"))
plt.close()

# =========================
# 5. Catplot: Тренды по годам
# =========================
g = sns.catplot(data=df_vis, x="year", y="value", hue="resource", col="metric",
                kind="point", ci=None, col_wrap=2)
g.set_xticklabels(rotation=45)
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Trends of energy metrics over time")
g.savefig(os.path.join(output_dir, "trends_over_time.png"))
plt.close()
