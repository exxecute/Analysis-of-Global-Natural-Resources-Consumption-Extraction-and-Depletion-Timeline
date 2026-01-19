# Analytical report on energy consumption data visualization

## 1. Quantitative data review (EDA)

At the current stage of data analysis, the distribution of observations across key categories has been assessed: resources, metrics, and regions. 

* **Resources and metrics:** The main data set focuses on fossil fuels (**Oil, Gas, Coal**). The **Production** metric prevails in the data set, accounting for more than 59% of all records. Emissions data accounts for only 6%, which is a bottleneck for environmental analysis.

![Distribution of observations by energy resource type](./../../../figures/data_visualization/count_by_resource.png)

* **Geography:** The highest data density is characteristic of the **Europe & Central Asia** region (more than 26,000 rows), while **North America** is represented minimally (about 2,000 rows), which is due to the small number of countries in the region.

![Volume of statistical data by global region](./../../../figures/data_visualization/count_by_region.png)

---

## 2. Analysis of value distribution

To understand the scale of consumption and production, a boxplot method with a logarithmic scale was used.

* **Dispersion:** The average value of the indicator is **198.54**, but the standard deviation exceeds **925**, indicating an extreme difference between the leading countries and the rest of the world.
* **Outliers:** A large number of points outside the whiskers (in the region of $10^4$) confirm that the global energy sector is heavily centered around a few major players.

![Distribution of value by resource (logarithmic scale)](./../../../figures/data_visualization/value_distribution_by_resource.png)

---

## 3. Historical trends: Oil consumption (1965–2024)

An analysis of time series data on total oil consumption reveals key geopolitical and economic shifts:

1. **Change in leadership:** The **East Asia & Pacific** region has shown aggressive growth since the 2000s, becoming the world's largest consumer.
2. **Western energy efficiency:** **North America** and **Europe** are showing stagnation or a decline in consumption, which may be due to the transition to renewable sources and increased production efficiency.
3. **The 2020 crisis:** The graph clearly shows a sharp “drop” in consumption in all regions caused by the COVID-19 pandemic, followed by a recovery.

![Dynamics of total oil consumption by region of the world](./../../../figures/data_visualization/oil_consumption_trend.png)
