import pandas as pd

def load_bp_sheet(path, sheet_name, resource, metric, unit, skiprows=2):
    """
    Универсальная функция для чтения листов BP Statistical Review.
    
    path: str — путь к Excel файлу
    sheet_name: str — название листа
    resource: str — ресурс (Oil, Gas, Coal и т.д.)
    metric: str — метрика (Reserves, Production, Consumption)
    unit: str — единицы измерения
    skiprows: int — сколько строк пропустить перед заголовком
    """
    # 1. Чтение Excel
    df = pd.read_excel(path, sheet_name=sheet_name, skiprows=skiprows)
    
    # 2. Чистим названия колонок
    df.columns = [str(c).strip() for c in df.columns]

    # 3. Колонка страны всегда первая
    country_col = df.columns[0]

    # 4. Года — все колонки начиная со второй
    year_cols = df.columns[1:]
    
    # 5. Melt в long-format
    df_long = df.melt(id_vars=[country_col], value_vars=year_cols,
                      var_name='year', value_name='value')

    # 6. Добавляем колонки для пайплайна
    df_long['resource'] = resource
    df_long['metric'] = metric
    df_long['unit'] = unit
    df_long['source'] = 'BP'
    df_long['iso_code'] = None

    # 7. Чистим пустые значения
    df_long = df_long.dropna(subset=['value'])

    # 8. Фильтруем агрегаты (Total, World)
    df_long = df_long[~df_long[country_col].str.contains('Total|World', na=False)]

    # 9. Переименовываем колонку страны
    df_long = df_long.rename(columns={country_col: 'country'})

    # 10. Приводим year к int (если возможно)
    try:
        df_long['year'] = df_long['year'].astype(int)
    except:
        # если там строки типа "1980*" — просто оставляем как есть
        df_long['year'] = df_long['year'].astype(str)

    return df_long


def load_bp(path):
    """
    Загружает все ключевые листы BP и объединяет их в один DataFrame.
    """
    dfs = []

    # --- Oil ---
    dfs.append(load_bp_sheet(path, 'Oil Production - barrels', 'Oil', 'Production', 'million barrels'))
    dfs.append(load_bp_sheet(path, 'Oil Consumption - EJ', 'Oil', 'Consumption', 'EJ'))

    # --- Gas ---
    dfs.append(load_bp_sheet(path, 'Gas - Proved reserves', 'Gas', 'Reserves', 'trillion cubic metres'))
    dfs.append(load_bp_sheet(path, 'Gas Production - Bcm', 'Gas', 'Production', 'Bcm'))
    dfs.append(load_bp_sheet(path, 'Gas Consumption - Bcm', 'Gas', 'Consumption', 'Bcm'))

    # --- Coal ---
    dfs.append(load_bp_sheet(path, 'Coal - Reserves', 'Coal', 'Reserves', 'Mt'))
    dfs.append(load_bp_sheet(path, 'Coal Production - mt', 'Coal', 'Production', 'Mt'))
    dfs.append(load_bp_sheet(path, 'Coal Consumption - EJ', 'Coal', 'Consumption', 'EJ'))

    # --- Nuclear ---
    dfs.append(load_bp_sheet(path, 'Nuclear Generation - TWh', 'Nuclear', 'Generation', 'TWh'))
    dfs.append(load_bp_sheet(path, 'Nuclear Consumption - EJ', 'Nuclear', 'Consumption', 'EJ'))

    # --- Hydro ---
    dfs.append(load_bp_sheet(path, 'Hydro Generation - TWh', 'Hydro', 'Generation', 'TWh'))
    dfs.append(load_bp_sheet(path, 'Hydro Consumption - EJ', 'Hydro', 'Consumption', 'EJ'))

    # --- Renewables ---
    dfs.append(load_bp_sheet(path, 'Renewables Consumption -EJ', 'Renewables', 'Consumption', 'EJ'))
    dfs.append(load_bp_sheet(path, 'Renewable Power (inc hydro) -EJ', 'Renewables', 'Power', 'EJ'))

    # --- Solar ---
    dfs.append(load_bp_sheet(path, 'Solar Generation - TWh', 'Solar', 'Generation', 'TWh'))
    dfs.append(load_bp_sheet(path, 'Solar Consumption - EJ', 'Solar', 'Consumption', 'EJ'))

    # --- Wind ---
    dfs.append(load_bp_sheet(path, 'Wind Generation - TWh', 'Wind', 'Generation', 'TWh'))
    dfs.append(load_bp_sheet(path, 'Wind Consumption - EJ', 'Wind', 'Consumption', 'EJ'))

    # --- Biofuels ---
    dfs.append(load_bp_sheet(path, 'Biofuels production - kboed', 'Biofuels', 'Production', 'kboed'))
    dfs.append(load_bp_sheet(path, 'Biofuels consumption - PJ', 'Biofuels', 'Consumption', 'PJ'))

    # --- Объединяем все в один DataFrame ---
    bp_long = pd.concat(dfs, ignore_index=True)

    return bp_long
