# Workflow

## Raw data preparation

- Added Our World in Data as a submodule
- Added BP/Energy Institute — Statistical Review of World Energy
- Added EIA (US Energy Information Administration):
  - Coal and coke consumption and production
  - Dry natural gas consumption and production
  - Electricity consumption, capacity, and production
  - Emissions by fuel type
  - Total energy consumption and production
  
## Data standardization
Table structure:
- country        – country
- iso_code       – ISO-3 code 
- region         – region 
- year           – year
- resource       – Oil | Gas | Coal | Electricity | Energy | CO2
- metric         – Consumption | Production | Reserves | Capacity | Emissions
- value          – numerical value
- unit           – unit of measurement
- source         – OWID | BP | EIA

## General pipeline
```pipeline
RAW DATA
│
├── OWID  ──┐
├── BP    ──┼── normalization → long format
├── EIA   ──┘
│
▼
HARMONIZATION
- countries
- years
- units
│
▼
energy_long.csv
```
## Rejection of EIA
During the normalization of datasets, I noticed
that EIA datasets are mostly empty and do not contain particularly important information,
so it was decided to reject this dataset.
## New unified table in progress
Table structure:
- country        – country
- iso_code       – ISO-3 code 
- region         – region 
- year           – year
- resource       – Oil | Gas | Coal | Electricity | Energy | CO2
- metric         – Consumption | Production | Reserves | Emissions
- value          – numerical value
- unit           – unit of measurement
- source         – OWID | BP
# Progress in cleaning and standardizing energy data
During the project, source information was collected from two main sources: **Our World in Data (OWID)** and **BP Energy Institute**. To standardize the data, a **table structure** was developed, including the following columns:
```
country, iso_code, region, year, resourc
