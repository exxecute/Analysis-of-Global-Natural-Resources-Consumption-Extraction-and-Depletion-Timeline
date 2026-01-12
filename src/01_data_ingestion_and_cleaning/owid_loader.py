import pandas as pd

def load_owid(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    keep = {
        "oil_consumption": ("Oil", "Consumption", "EJ"),
        "gas_consumption": ("Gas", "Consumption", "EJ"),
        "coal_consumption": ("Coal", "Consumption", "EJ"),
        "energy_consumption": ("Energy", "Consumption", "EJ"),
        "co2": ("CO2", "Emissions", "MtCO2")
    }

    rows = []

    for col, (res, met, unit) in keep.items():
        if col not in df.columns:
            continue

        tmp = df[["country", "iso_code", "year", col]].dropna()
        tmp["resource"] = res
        tmp["metric"] = met
        tmp["unit"] = unit
        tmp["value"] = tmp[col]
        tmp["source"] = "OWID"

        rows.append(
            tmp[["country", "iso_code", "year", "resource", "metric", "value", "unit", "source"]]
        )

    return pd.concat(rows, ignore_index=True)
