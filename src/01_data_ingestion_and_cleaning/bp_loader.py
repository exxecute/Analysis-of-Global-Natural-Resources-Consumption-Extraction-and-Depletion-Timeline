import pandas as pd

def load_bp_oil_reserves(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="Oil - Proved reserves")

    df = df.rename(columns={
        "Country": "country",
        "Year": "year",
        "Reserves": "value"
    })

    df["resource"] = "Oil"
    df["metric"] = "Reserves"
    df["unit"] = "billion barrels"
    df["source"] = "BP"
    df["iso_code"] = None

    return df[[
        "country", "iso_code", "year",
        "resource", "metric", "value", "unit", "source"
    ]].dropna(subset=["value"])
