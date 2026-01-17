import pandas as pd

# Загрузка датасета
df = pd.read_csv("../../data/processed/energy_panel_clean.csv")

# ----------------------------
# 1. Общая информация
# ----------------------------
print("=== Общая информация ===")
print(df.info())
print("\nОбщие строки/колонки:", df.shape)
print("\nПропуски по колонкам:\n", df.isna().sum())

# ----------------------------
# 2. Уникальные значения
# ----------------------------
print("\n=== Уникальные значения ===")
print("Ресурсы:", df['resource'].unique())
print("Метрики:", df['metric'].unique())
print("Страны:", df['country'].nunique())
print("Регионы:", df['region'].unique())
print("Годы:", df['year'].min(), "-", df['year'].max())

# ----------------------------
# 3. Статистика по value
# ----------------------------
print("\n=== Статистика по 'value' ===")
print(df['value'].describe())

# ----------------------------
# 4. Количество наблюдений по категориям
# ----------------------------
print("\n=== Количество наблюдений ===")
print("По ресурсам:\n", df['resource'].value_counts())
print("По метрикам:\n", df['metric'].value_counts())
print("По регионам:\n", df['region'].value_counts())

# ----------------------------
# 5. Проверка на дубликаты и отрицательные значения
# ----------------------------
print("\n=== Дубликаты и отрицательные значения ===")
print("Дубликаты:", df.duplicated(subset=['country','year','resource','metric']).sum())
print("Отрицательные значения в 'value':", (df['value'] < 0).sum())
