import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# =========================
# Настройки
# =========================
ALPHA = 0.05
OUTPUT_DIR = "../../figures/hypothesis_tests/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Загружаем очищенный датасет
df = pd.read_csv("../../data/processed/energy_panel_clean.csv")

resources = df['resource'].unique()
metrics = df['metric'].unique()

results = []

# =========================
# Проверка гипотез и визуализация
# =========================
for resource in resources:
    for metric in metrics:
        df_sub = df[(df['resource'] == resource) & (df['metric'] == metric)]
        if df_sub.empty:
            continue

        # --- ANOVA по регионам ---
        groups = [group['value'].values for _, group in df_sub.groupby('region') if len(group) > 0]
        if len(groups) > 1:
            try:
                f_stat, p_val = stats.f_oneway(*groups)
                significant = p_val < ALPHA
                results.append({
                    'resource': resource,
                    'metric': metric,
                    'test': 'ANOVA_regions',
                    'stat': f_stat,
                    'p_value': p_val,
                    'significant': significant
                })

                # --- Boxplot регионов ---
                plt.figure(figsize=(10,6))
                sns.boxplot(x='region', y='value', data=df_sub)
                plt.title(f"{resource} - {metric} by region (ANOVA p={p_val:.3f})")
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}{resource}_{metric}_anova_regions.png")
                plt.close()
            except Exception as e:
                print(f"ANOVA error for {resource}-{metric}: {e}")

        # --- T-test между двумя крупнейшими странами ---
        top_countries = df_sub.groupby('country')['value'].sum().nlargest(2).index.tolist()
        if len(top_countries) == 2:
            try:
                group1 = df_sub[df_sub['country'] == top_countries[0]]['value']
                group2 = df_sub[df_sub['country'] == top_countries[1]]['value']
                t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
                significant = p_val < ALPHA
                results.append({
                    'resource': resource,
                    'metric': metric,
                    'test': f"T-test_{top_countries[0]}_vs_{top_countries[1]}",
                    'stat': t_stat,
                    'p_value': p_val,
                    'significant': significant
                })

                # --- Barplot двух стран ---
                df_bar = df_sub[df_sub['country'].isin(top_countries)]
                df_bar_sum = df_bar.groupby('country')['value'].sum().reset_index()
                plt.figure(figsize=(6,4))
                sns.barplot(x='country', y='value', data=df_bar_sum)
                plt.title(f"{resource} - {metric} Top 2 Countries (T-test p={p_val:.3f})")
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}{resource}_{metric}_t_test_top_countries.png")
                plt.close()
            except Exception as e:
                print(f"T-test error for {resource}-{metric}: {e}")

# =========================
# Сохраняем результаты
# =========================
df_results = pd.DataFrame(results)
df_results.to_csv(f"{OUTPUT_DIR}hypothesis_tests_results.csv", index=False)
print("Hypothesis testing completed. Results saved to CSV and plots.")
