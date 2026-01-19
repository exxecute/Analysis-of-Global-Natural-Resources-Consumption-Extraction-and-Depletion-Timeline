# Analytical report on the energy consumption dataset

## General information
- The dataset contains **80,639 observations** and 11 columns.
- There are missing values in `iso_code` (≈466–20,137) and `region` (466), the rest of the columns are filled in.
- There are **duplicates**: 20,811 rows. It is worth checking that these are not repeated measurements for the same country, resource, metric, and year.
- **Negative values** in `value`: 168. These may be measurement errors or data corrections (e.g., consumption/production rollbacks).

## Resources and metrics
- Four resources are used: **Oil, Gas, Coal, CO2**.
- Metrics: **Production, Consumption, Emissions**.
- By number of observations:
  - **Production** — 47,406 rows (≈59%),
  - **Consumption** — 28,083 rows (≈35%),
  - **Emissions** — 5,150 rows (≈6%).
- The resource with the highest number of observations is **Oil** (26,214 rows), and the lowest is **CO2** (5,150).

## Geography and regions
- Data covers **217 countries**, including regional aggregations.
- Main regions:
  - Europe & Central Asia — 26,803 observations
  - East Asia & Pacific — 13,875
  - Latin America & Caribbean — 13,157
  - Middle East & North Africa — 11,276
  - Sub-Saharan Africa — 9,269
  - South Asia — 3,797
  - North America — 1,996
- There are **466 countries without a specified region**.

## Time coverage
- Data by year: **1900–2024**.
- This allows for long-term analysis of historical trends in consumption, production, and emissions.

## Indicator values
- Average value: **198.54**.
- High dispersion: **standard deviation ≈ 925**, indicating a wide range of data (including large countries with huge consumption/production).
- Minimum values may be negative (168 rows) — potentially errors or adjustments.
- Maximum values reach 26,245, probably large indicators for countries with large populations and energy consumption.

## Initial conclusions
1. **The dataset is high quality**.
2. There are few CO2 observations — this should be taken into account when analyzing emissions.
3. Most of the data is concentrated in Europe, Asia, and Latin America; North America is less represented.
