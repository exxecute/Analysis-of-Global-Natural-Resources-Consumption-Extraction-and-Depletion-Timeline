import pandas as pd

def load_owid(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    
    mapping = { # TODO: refactor to common
        # Общие показатели
        "population": ("Population", "Total", "million"),
        "gdp": ("GDP", "Total", "billion_USD"),
        "per_capita_electricity": ("Electricity", "Per Capita", "kWh"),
        "energy_per_capita": ("Energy", "Per Capita", "GJ"),
        "energy_per_gdp": ("Energy", "Per GDP", "GJ/US$"),
        "primary_energy_consumption": ("Energy", "Total", "EJ"),
        
        # Фоссильные топлива
        "fossil_fuel_consumption": ("Fossil Fuels", "Consumption", "EJ"),
        "fossil_energy_per_capita": ("Fossil Fuels", "Per Capita", "GJ"),
        "fossil_electricity": ("Fossil Fuels", "Electricity", "TWh"),
        "fossil_elec_per_capita": ("Fossil Fuels", "Electricity Per Capita", "kWh"),
        "fossil_cons_change_pct": ("Fossil Fuels", "Consumption Change %", "%"),
        "fossil_cons_change_twh": ("Fossil Fuels", "Consumption Change TWh", "TWh"),
        "fossil_share_elec": ("Fossil Fuels", "Share of Electricity", "%"),
        "fossil_share_energy": ("Fossil Fuels", "Share of Energy", "%"),
        
        # Нефть
        "oil_consumption": ("Oil", "Consumption", "EJ"),
        "oil_production": ("Oil", "Production", "EJ"),
        "oil_prod_per_capita": ("Oil", "Production Per Capita", "GJ"),
        "oil_prod_change_pct": ("Oil", "Production Change %", "%"),
        "oil_prod_change_twh": ("Oil", "Production Change TWh", "TWh"),
        "oil_share_elec": ("Oil", "Share of Electricity", "%"),
        "oil_share_energy": ("Oil", "Share of Energy", "%"),
        "oil_energy_per_capita": ("Oil", "Energy Per Capita", "GJ"),
        "oil_elec_per_capita": ("Oil", "Electricity Per Capita", "kWh"),
        
        # Газ
        "gas_consumption": ("Gas", "Consumption", "EJ"),
        "gas_production": ("Gas", "Production", "EJ"),
        "gas_prod_per_capita": ("Gas", "Production Per Capita", "GJ"),
        "gas_prod_change_pct": ("Gas", "Production Change %", "%"),
        "gas_prod_change_twh": ("Gas", "Production Change TWh", "TWh"),
        "gas_share_elec": ("Gas", "Share of Electricity", "%"),
        "gas_share_energy": ("Gas", "Share of Energy", "%"),
        "gas_energy_per_capita": ("Gas", "Energy Per Capita", "GJ"),
        "gas_elec_per_capita": ("Gas", "Electricity Per Capita", "kWh"),
        
        # Уголь
        "coal_consumption": ("Coal", "Consumption", "EJ"),
        "coal_production": ("Coal", "Production", "EJ"),
        "coal_prod_per_capita": ("Coal", "Production Per Capita", "GJ"),
        "coal_prod_change_pct": ("Coal", "Production Change %", "%"),
        "coal_prod_change_twh": ("Coal", "Production Change TWh", "TWh"),
        "coal_share_elec": ("Coal", "Share of Electricity", "%"),
        "coal_share_energy": ("Coal", "Share of Energy", "%"),
        "coal_energy_per_capita": ("Coal", "Energy Per Capita", "GJ"),
        "coal_elec_per_capita": ("Coal", "Electricity Per Capita", "kWh"),
        
        # Электроэнергия
        "electricity_generation": ("Electricity", "Generation", "TWh"),
        "electricity_demand": ("Electricity", "Demand", "TWh"),
        "electricity_demand_per_capita": ("Electricity", "Demand Per Capita", "kWh"),
        
        # Возобновляемая энергия
        "renewables_consumption": ("Renewables", "Consumption", "EJ"),
        "renewables_electricity": ("Renewables", "Electricity", "TWh"),
        "renewables_energy_per_capita": ("Renewables", "Per Capita", "GJ"),
        "renewables_elec_per_capita": ("Renewables", "Electricity Per Capita", "kWh"),
        "renewables_share_elec": ("Renewables", "Share of Electricity", "%"),
        "renewables_share_energy": ("Renewables", "Share of Energy", "%"),
        "renewables_cons_change_pct": ("Renewables", "Consumption Change %", "%"),
        "renewables_cons_change_twh": ("Renewables", "Consumption Change TWh", "TWh"),
        
        # Биоэнергия
        "biofuel_consumption": ("Biofuel", "Consumption", "EJ"),
        "biofuel_electricity": ("Biofuel", "Electricity", "TWh"),
        "biofuel_elec_per_capita": ("Biofuel", "Electricity Per Capita", "kWh"),
        "biofuel_cons_per_capita": ("Biofuel", "Consumption Per Capita", "GJ"),
        "biofuel_share_elec": ("Biofuel", "Share of Electricity", "%"),
        "biofuel_share_energy": ("Biofuel", "Share of Energy", "%"),
        "biofuel_cons_change_pct": ("Biofuel", "Consumption Change %", "%"),
        "biofuel_cons_change_twh": ("Biofuel", "Consumption Change TWh", "TWh"),
        
        # Гидроэнергия
        "hydro_consumption": ("Hydro", "Consumption", "EJ"),
        "hydro_electricity": ("Hydro", "Electricity", "TWh"),
        "hydro_energy_per_capita": ("Hydro", "Energy Per Capita", "GJ"),
        "hydro_elec_per_capita": ("Hydro", "Electricity Per Capita", "kWh"),
        "hydro_share_elec": ("Hydro", "Share of Electricity", "%"),
        "hydro_share_energy": ("Hydro", "Share of Energy", "%"),
        "hydro_cons_change_pct": ("Hydro", "Consumption Change %", "%"),
        "hydro_cons_change_twh": ("Hydro", "Consumption Change TWh", "TWh"),
        
        # Ядерная энергия
        "nuclear_consumption": ("Nuclear", "Consumption", "EJ"),
        "nuclear_electricity": ("Nuclear", "Electricity", "TWh"),
        "nuclear_energy_per_capita": ("Nuclear", "Energy Per Capita", "GJ"),
        "nuclear_elec_per_capita": ("Nuclear", "Electricity Per Capita", "kWh"),
        "nuclear_share_elec": ("Nuclear", "Share of Electricity", "%"),
        "nuclear_share_energy": ("Nuclear", "Share of Energy", "%"),
        "nuclear_cons_change_pct": ("Nuclear", "Consumption Change %", "%"),
        "nuclear_cons_change_twh": ("Nuclear", "Consumption Change TWh", "TWh"),
        
        # Солнечная энергия
        "solar_consumption": ("Solar", "Consumption", "EJ"),
        "solar_electricity": ("Solar", "Electricity", "TWh"),
        "solar_energy_per_capita": ("Solar", "Energy Per Capita", "GJ"),
        "solar_elec_per_capita": ("Solar", "Electricity Per Capita", "kWh"),
        "solar_share_elec": ("Solar", "Share of Electricity", "%"),
        "solar_share_energy": ("Solar", "Share of Energy", "%"),
        "solar_cons_change_pct": ("Solar", "Consumption Change %", "%"),
        "solar_cons_change_twh": ("Solar", "Consumption Change TWh", "TWh"),
        
        # Ветровая энергия
        "wind_consumption": ("Wind", "Consumption", "EJ"),
        "wind_electricity": ("Wind", "Electricity", "TWh"),
        "wind_energy_per_capita": ("Wind", "Energy Per Capita", "GJ"),
        "wind_elec_per_capita": ("Wind", "Electricity Per Capita", "kWh"),
        "wind_share_elec": ("Wind", "Share of Electricity", "%"),
        "wind_share_energy": ("Wind", "Share of Energy", "%"),
        "wind_cons_change_pct": ("Wind", "Consumption Change %", "%"),
        "wind_cons_change_twh": ("Wind", "Consumption Change TWh", "TWh"),
        
        # Прочие возобновляемые
        "other_renewable_consumption": ("Other Renewables", "Consumption", "EJ"),
        "other_renewable_electricity": ("Other Renewables", "Electricity", "TWh"),
        "other_renewables_cons_change_pct": ("Other Renewables", "Consumption Change %", "%"),
        "other_renewables_cons_change_twh": ("Other Renewables", "Consumption Change TWh", "TWh"),
        "other_renewables_elec_per_capita": ("Other Renewables", "Electricity Per Capita", "kWh"),
        "other_renewables_elec_per_capita_exc_biofuel": ("Other Renewables", "Electricity Per Capita Exc Biofuel", "kWh"),
        "other_renewables_energy_per_capita": ("Other Renewables", "Energy Per Capita", "GJ"),
        "other_renewables_share_elec": ("Other Renewables", "Share of Electricity", "%"),
        "other_renewables_share_elec_exc_biofuel": ("Other Renewables", "Share of Electricity Exc Biofuel", "%"),
        "other_renewables_share_energy": ("Other Renewables", "Share of Energy", "%"),
        
        # Карбон / выбросы
        "carbon_intensity_elec": ("Electricity", "Carbon Intensity", "kgCO2/kWh"),
        "greenhouse_gas_emissions": ("CO2", "Emissions", "MtCO2"),
        
        # Прочие показатели
        "electricity_share_energy": ("Electricity", "Share of Energy", "%"),
        "net_elec_imports": ("Electricity", "Net Imports", "TWh"),
        "net_elec_imports_share_demand": ("Electricity", "Net Imports Share of Demand", "%")
    }

    rows = []

    for col, (res, met, unit) in mapping.items():
        if col in df.columns:
            tmp = df[["country", "iso_code", "year", col]].dropna()
            tmp["resource"] = res
            tmp["metric"] = met
            tmp["unit"] = unit
            tmp["value"] = tmp[col]
            tmp["source"] = "OWID"
            rows.append(tmp[["country","iso_code","year","resource","metric","value","unit","source"]])
    
    df_long = pd.concat(rows, ignore_index=True)
    return df_long
