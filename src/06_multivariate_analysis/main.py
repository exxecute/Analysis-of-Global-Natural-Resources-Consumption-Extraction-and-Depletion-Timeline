import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

# =========================
# Настройки
# =========================
DATA_PATH = "../../data/processed/energy_panel_clean.csv"
NUMERIC_METRICS = ["Production", "Consumption", "Emissions"]
OUTPUT_MAIN = "../../figures/multivariate_analysis/pca_main.png"
OUTPUT_OUTLIERS = "../../figures/multivariate_analysis/pca_outliers.png"

# =========================
# Загрузка данных
# =========================
df = pd.read_csv(DATA_PATH)
df_numeric = df[df["metric"].isin(NUMERIC_METRICS)].copy()

df_pivot = df_numeric.pivot_table(
    index='country',
    columns=['resource', 'metric'],
    values='value',
    aggfunc='sum',
    fill_value=0
)

# =========================
# Масштабирование и PCA
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_pivot)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'], index=df_pivot.index)

explained = pca.explained_variance_ratio_
print(f"Доля объясненной дисперсии: PC1={explained[0]:.2f}, PC2={explained[1]:.2f}")

# =========================
# Делим на основную массу и выбросы
# =========================
pc1_95 = np.percentile(df_pca['PC1'], 95)
pc2_95 = np.percentile(df_pca['PC2'], 95)

main_mask = (df_pca['PC1'] <= pc1_95) & (df_pca['PC2'] <= pc2_95)
df_main = df_pca[main_mask]
df_outliers = df_pca[~main_mask]

# =========================
# Функция для визуализации
# =========================
def plot_pca(df_plot, file_name, title):
    plt.figure(figsize=(12,8))
    plt.scatter(df_plot['PC1'], df_plot['PC2'], alpha=0.7, c='skyblue', edgecolor='k')
    for country in df_plot.index[:20]:  # подписи для первых 20 стран
        plt.text(df_plot.loc[country, 'PC1'], df_plot.loc[country, 'PC2'], country, fontsize=8)
    plt.xlabel(f'PC1 ({explained[0]*100:.1f}% дисперсии)')
    plt.ylabel(f'PC2 ({explained[1]*100:.1f}% дисперсии)')
    plt.title(title)
    plt.grid(True)
    plt.savefig(file_name, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved PCA plot: {file_name}")

# =========================
# Сохраняем графики
# =========================
plot_pca(df_main, OUTPUT_MAIN, "PCA (Основная масса стран, 0-95 перцентиль)")
plot_pca(df_outliers, OUTPUT_OUTLIERS, "PCA (Выбросы стран, >95 перцентиль)")
