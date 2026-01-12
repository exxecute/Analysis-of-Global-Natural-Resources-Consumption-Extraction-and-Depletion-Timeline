from owid_loader import load_owid
from bp_loader import load_bp_oil_reserves
from eia_loader import load_eia_generic
import pandas as pd

def run_pipeline():

    dfs = []

    dfs.append(
        load_owid("../../data/raw/our-world-in-data/owid-energy-data.csv")
    )

    # dfs.append(
    #     load_bp_oil_reserves("../../data/raw/bp/bp_statistical_review.xlsx")
    # )

    # dfs.append(
    #     load_eia_generic(
    #         "../../data/raw/eia/gas_consumption.csv",
    #         resource="Gas",
    #         metric="Consumption",
    #         unit="EJ"
    #     )
    # )

    energy_long = pd.concat(dfs, ignore_index=True)

    energy_long.to_csv(
        "../../data/intermediate/energy_long.csv",
        index=False
    )

if __name__ == "__main__":
    run_pipeline()
