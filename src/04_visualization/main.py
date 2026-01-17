import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# Папка для сохранения графиков
# =========================
output_dir = "../../figures/data_visualization"
os.makedirs(output_dir, exist_ok=True)

# =========================
# Загрузка датасета
# =========================
df = pd.read_csv("../../data/processed/energy_panel_clean.csv")

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# =========================
# 1. Количество наблюдений по ресурсам
# =========================
plt.figure()
sns.countplot(data=df, x="resource", order=df["resource"].value_counts().index)
plt.title("Количество наблюдений по ресурсам")
plt.ylabel("Количество строк")
plt.xlabel("Ресурс")
plt.tight_layout()
plt.savefig(f"{output_dir}/count_by_resource.png")
plt.close()

# =========================
# 2. Количество наблюдений по метрикам
# =========================
plt.figure()
sns.countplot(data=df, x="metric", order=df["metric"].value_counts().index)
plt.title("Количество наблюдений по метрикам")
plt.ylabel("Количество строк")
plt.xlabel("Метрика")
plt.tight_layout()
plt.savefig(f"{output_dir}/count_by_metric.png")
plt.close()

# =========================
# 3. Распределение value по ресурсам
# =========================
plt.figure()
sns.boxplot(data=df[df["value"] >= 0], x="resource", y="value")
plt.title("Распределение значений value по ресурсам (без отрицательных)")
plt.yscale("log")
plt.tight_layout()
plt.savefig(f"{output_dir}/value_distribution_by_resource.png")
plt.close()

# =========================
# 4. Количество наблюдений по регионам
# =========================
plt.figure()
sns.countplot(data=df, y="region", order=df["region"].value_counts().index)
plt.title("Количество наблюдений по регионам")
plt.xlabel("Количество строк")
plt.ylabel("Регион")
plt.tight_layout()
plt.savefig(f"{output_dir}/count_by_region.png")
plt.close()

# =========================
# 5. Тренд потребления нефти по регионам
# =========================
plt.figure()
oil_consumption = df[(df["resource"]=="Oil") & (df["metric"]=="Consumption")]
sns.lineplot(data=oil_consumption, x="year", y="value", hue="region", estimator="sum")
plt.title("Тренд потребления нефти по регионам")
plt.ylabel("Суммарное потребление")
plt.xlabel("Год")
plt.tight_layout()
plt.savefig(f"{output_dir}/oil_consumption_trend.png")
plt.close()

print("Все графики сохранены в папку:", output_dir)
