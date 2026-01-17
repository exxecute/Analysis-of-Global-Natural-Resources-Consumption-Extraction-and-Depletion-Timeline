import pandas as pd

# =========================
# CONFIG
# =========================

ALLOWED_RESOURCES = {
    "Oil", "Gas", "Coal", "Electricity", "Energy", "CO2"
}

RESOURCE_MAP = {
    # Fossil fuels
    "Oil": "Oil",
    "Gas": "Gas",
    "Coal": "Coal",
    "Fossil Fuels": "Fossil Fuels",

    # Electricity / Energy
    "Electricity": "Electricity",
    "Energy": "Energy",

    # Low-carbon
    "Nuclear": "Nuclear",
    "Hydro": "Hydro",
    "Renewables": "Renewables",
    "Biofuel": "Biofuels",
    "Biofuels": "Biofuels",
    "Solar": "Solar",
    "Wind": "Wind",
    "Other Renewables": "Other Renewables",

    # Emissions
    "CO2": "CO2"
}

def filter_resources(df: pd.DataFrame) -> pd.DataFrame:
    """
    Оставляет только ресурсы, используемые в проекте
    """
    before = df.shape[0]

    df = df[df["resource"].isin(ALLOWED_RESOURCES)].copy()

    after = df.shape[0]
    print(f"[filter_resources] rows before: {before}, after: {after}")

    return df

def normalize_resource(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["resource"] = df["resource"].apply(
        lambda x: RESOURCE_MAP.get(x)
    )
    return df

def assert_no_nan_resources(df: pd.DataFrame) -> None:
    if df["resource"].isna().any():
        bad = df[df["resource"].isna()]
        raise ValueError(
            f"Unmapped resource values detected:\n{bad['resource'].unique()}"
        )

ALLOWED_METRICS = {
    "Consumption", "Production", "Reserves", "Emissions"
}

def filter_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Оставляет только метрики, используемые в проекте
    """
    before = df.shape[0]

    df = df[df["metric"].isin(ALLOWED_METRICS)].copy()

    after = df.shape[0]
    print(f"[filter_metrics] rows before: {before}, after: {after}")

    return df


AGGREGATES = [
    "World", "OECD", "Non-OECD", "EU",
    "Total", "Other", "Asia", "Europe",
    "Middle East", "Africa", "Americas",
    "Asia Pacific"
]

MANUAL_ISO_FIXES = {
    "United States": "USA",
    "US": "USA",
    "Russia": "RUS",
    "Iran": "IRN",
    "Venezuela": "VEN",
    "South Korea": "KOR",
    "North Korea": "PRK",
    "Czech Republic": "CZE",
    "Slovakia": "SVK",
    "Vietnam": "VNM"
}

# =========================
# VALIDATION
# =========================

def validate_schema(df: pd.DataFrame) -> None:
    required = {
        "country", "iso_code", "region",
        "year", "resource", "metric",
        "value", "unit", "source"
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if not df["resource"].isin(ALLOWED_RESOURCES).all():
        print("Unique resource values:")
        print(sorted(df["resource"].unique()))
        raise ValueError("Invalid resource values detected")

    if not df["metric"].isin(ALLOWED_METRICS).all():
        print("Unique metrics values:")
        print(sorted(df["metric"].unique()))
        raise ValueError("Invalid metric values detected")

    if not df["year"].between(1800, 2100).all():
        raise ValueError("Year out of range")

    if not pd.api.types.is_numeric_dtype(df["value"]):
        raise ValueError("Value column must be numeric")


# =========================
# CLEANING
# =========================

def drop_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    pattern = "|".join(AGGREGATES)
    return df[~df["country"].str.contains(pattern, na=False)]


def fix_iso_codes(df: pd.DataFrame) -> pd.DataFrame:
    df["iso_code"] = df.apply(
        lambda r: MANUAL_ISO_FIXES.get(r["country"], r["iso_code"]),
        axis=1
    )
    return df


# =========================
# REGION MERGE
# =========================

def add_regions(
    df: pd.DataFrame,
    regions: pd.DataFrame
) -> pd.DataFrame:
    """
    regions: country | iso_code | region
    """

    df = df.merge(
        regions,
        on=["country", "iso_code"],
        how="left"
    )

    return df


# =========================
# QUALITY CHECKS
# =========================

def quality_checks(df: pd.DataFrame) -> None:
    print("Duplicates:",
          df.duplicated(
              ["country", "year", "resource", "metric", "source"]
          ).sum())

    print("Negative values:",
          (df["value"] < 0).sum())

    missing_regions = df[df["region"].isna()]["country"].unique()
    print(f"Countries without region ({len(missing_regions)}):")
    print(missing_regions)


# =========================
# MAIN PIPELINE
# =========================

def run_cleaning_pipeline() -> None:
    ALLOWED_RESOURCES = set(RESOURCE_MAP.values())
    
    print("Loading intermediate dataset...")
    df = pd.read_csv(
        "../../data/intermediate/energy_long.csv"
    )

    print("Dropping aggregates...")
    df = drop_aggregates(df)

    print("Fixing ISO codes...")
    df = fix_iso_codes(df)

    print("Normalizing resource names...")
    df = normalize_resource(df)

    print("Filtering resource names...")
    df = filter_resources(df)

    print("Checking unmapped resources...")
    assert_no_nan_resources(df)

    print("Filtering metrics names...")
    df = filter_metrics(df)

    print("Loading country-region mapping...")
    regions = pd.read_csv(
        "../../data/reference/country_regions.csv"
    )

    print("Adding regions...")
    df = add_regions(df, regions)

    print("Validating schema...")
    validate_schema(df)

    print("Running quality checks...")
    quality_checks(df)

    print("Saving processed dataset...")
    df.to_csv(
        "../../data/processed/energy_panel_clean.csv",
        index=False
    )

    print("Pipeline completed successfully.")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    run_cleaning_pipeline()
