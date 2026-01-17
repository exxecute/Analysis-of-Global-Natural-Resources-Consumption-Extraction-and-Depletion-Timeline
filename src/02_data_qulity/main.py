import pandas as pd

# =========================
# CONFIG
# =========================

ALLOWED_RESOURCES = {
    "Oil", "Gas", "Coal", "Electricity", "Energy", "CO2"
}

ALLOWED_METRICS = {
    "Consumption", "Production", "Reserves", "Emissions"
}

AGGREGATES = [
    "World", "OECD", "Non-OECD", "EU",
    "Total", "Other", "Asia", "Europe",
    "Middle East", "Africa", "Americas",
    "Asia Pacific"
]

MANUAL_COUNTRY_MAP = {
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
    required_cols = {
        "country", "iso_code", "region", "year",
        "resource", "metric", "value", "unit", "source"
    }

    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if not df["resource"].isin(ALLOWED_RESOURCES).all():
        raise ValueError("Invalid values in resource")

    if not df["metric"].isin(ALLOWED_METRICS).all():
        raise ValueError("Invalid values in metric")

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


def apply_manual_country_map(df: pd.DataFrame) -> pd.DataFrame:
    df["iso_code"] = df.apply(
        lambda r: MANUAL_COUNTRY_MAP.get(r["country"], r["iso_code"]),
        axis=1
    )
    return df


# =========================
# NORMALIZATION
# =========================

def normalize_countries(
    df: pd.DataFrame,
    owid_ref: pd.DataFrame
) -> pd.DataFrame:
    """
    owid_ref must contain: country, iso_code, region
    """

    ref = (
        owid_ref[["country", "iso_code", "region"]]
        .drop_duplicates()
    )

    df = df.merge(
        ref,
        on="country",
        how="left",
        suffixes=("", "_ref")
    )

    df["iso_code"] = df["iso_code"].fillna(df["iso_code_ref"])
    df["region"] = df["region"].fillna(df["region_ref"])

    df = df.drop(columns=["iso_code_ref", "region_ref"])

    df = apply_manual_country_map(df)

    return df


# =========================
# QUALITY CHECKS
# =========================

def quality_checks(df: pd.DataFrame) -> None:
    dupes = df.duplicated(
        subset=["country", "year", "resource", "metric", "source"]
    )
    print(f"Duplicates: {dupes.sum()}")

    negative = df[df["value"] < 0]
    print(f"Negative values: {len(negative)}")

    missing_iso = df[df["iso_code"].isna()]["country"].unique()
    print(f"Countries without ISO ({len(missing_iso)}):")
    print(missing_iso)


# =========================
# MAIN PIPELINE
# =========================

def run_cleaning_pipeline() -> None:
    print("Loading intermediate data...")
    df = pd.read_csv(
        "../../data/intermediate/energy_long.csv"
    )

    print("Loading OWID reference...")
    owid_ref = pd.read_csv(
        "../../data/raw/our-world-in-data/owid-energy-data.csv",
        usecols=["country", "iso_code", "region"]
    )

    print("Dropping aggregates...")
    df = drop_aggregates(df)

    print("Normalizing countries...")
    df = normalize_countries(df, owid_ref)

    print("Validating schema...")
    validate_schema(df)

    print("Running quality checks...")
    quality_checks(df)

    print("Saving clean dataset...")
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
