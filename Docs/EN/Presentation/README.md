# Presentation of the topic

## 1. Project title
**Analysis of Global Natural Resources: Consumption, Extraction, and Depletion Forecasting**

---

## 2. Project objective
- To investigate current reserves and extraction rates of natural resources (oil, gas, coal, water, food, energy in general).  
- Determine the dynamics of resource consumption by country and region.  
- Forecast the time of possible resource depletion at current consumption rates.  
- Conduct visual and statistical analysis of data, including PCA and clustering.  
- Provide recommendations for the rational use of resources.

---

## 3. Justification for choosing this topic
- **Relevance:** The depletion of natural resources and climate change are global challenges.  
- **Data availability:** The World Bank, BP Statistical Review, FAO, and Our World in Data provide high-quality public data.  
- **Analysis methods:** The project allows the use of EDA, visualization, statistical tests, PCA, and clustering.
- **Educational value:** Demonstration of skills in working with Python and R, analytical and statistical thinking.


---

## 4. Methods and tools

| Project stage | Tool | Methods |
|-------------|------------|--------|
| Preliminary analysis | Python (pandas, numpy) | Descriptive statistics, data verification, handling missing values |
| Visualization | Python (matplotlib, seaborn) | Histograms, boxplots, violin plots, scatter plots, cat plots |
| Hypothesis testing | Python (stats, t.test, ANOVA, chisq.test) | t-test, ANOVA, χ², region comparison |
| Multivariate analysis | Python (scikit-learn) | PCA, KMeans, clustering, principal component visualization |
| Depletion forecast | Python  | Consumption extrapolation, calculation of “Years to depletion” |

---

## 5. Expected results
- Tables and graphs showing the distribution of reserves and consumption of resources by country and region.
- Visualization of consumption trends over recent years.
- Identification of countries with high and low levels of consumption and resource security.  
- Clusters of countries with similar resource profiles.
- Forecast of when key resources may be depleted at current consumption rates.
- Recommendations for rational resource use.

---

## 6. Brief analysis diagram

```scheme
+--------------------+
| Global data        |
+--------------------+
          |
          v
+--------------------+
| Descriptive Stats  |
| (Python pandas)    |
+--------------------+
          |
          v
+--------------------+
| Visual Analysis    |
| (Python seaborn)   |
+--------------------+
          |
          v
+--------------------+
| Hypothesis Testing |
| (Python)           |
+--------------------+
          |
          v
+--------------------+
| PCA & Clustering   |
| (Python sklearn)   |
+--------------------+
          |
          v
+--------------------+
| Depletion Forecast |
| (Python)           |
+--------------------+
          |
          v
+--------------------+
| Insights & Report |
+--------------------+
```

---

## 7. Project advantages
- **Interdisciplinarity:** combines energy, ecology, and economics.
- **Comprehensiveness:** includes EDA, visualization, statistics, PCA, clustering, and forecasting.  
- **Scientific and practical significance:** identifies threats of resource depletion and analyzes consumption by country.  

---

## 8. Next steps
1. Selection and consolidation of datasets for selected resources.  
2. Initial analysis and data cleaning.  
3. Visualization and study of resource distributions.  
4. Testing hypotheses about differences between countries and regions.  
5. PCA and clustering of countries by resource profile.  
6. Forecast of resource depletion time.  
7. Preparation of a final report and presentation.
