import pandas as pd

def load_eia_generic(path: str, resource, metric, unit) -> pd.DataFrame:
    df = pd.read_csv(path)

    df = df.rename(columns={
        "Country": "country",
        "Year": "year",
        "Value": "value"
    })

    df["resource"] = resource
    df["metric"] = metric
    df["unit"] = unit
    df["source"] = "EIA"
    df["iso_code"] = None

    return df[[
        "country", "iso_code", "year",
        "resource", "metric", "value", "unit", "source"
    ]].dropna(subset=["value"])
