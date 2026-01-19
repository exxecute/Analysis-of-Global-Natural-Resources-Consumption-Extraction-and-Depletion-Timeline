# Analysis of Global Natural Resources: Consumption, Extraction, and Depletion Timeline

## Overview

This repository was created to support a data analysis project focused on the consumption, extraction, and depletion timelines of natural resources.
The project also serves as an academic data analysis assignment developed within the context of a university course.

## Features

- Analyze patterns of natural resource consumption and extraction
- Estimate and visualize resource depletion timelines
- Apply data analysis techniques to real-world datasets
- Fulfill academic requirements for a university data analysis project

## Tools & Technologies

This project may utilize:
- Python 3.12 (security)
  - contourpy 1.3.3
  - cycler 0.12.1
  - et_xmlfile 2.0.0
  - fonttools 4.61.1
  - joblib 1.5.3
  - kiwisolver 1.4.9
  - matplotlib 3.10.8
  - numpy 2.4.1
  - openpyxl 3.1.5
  - packaging 25.0
  - pandas 2.3.3
  - pillow 12.1.0
  - pyparsing 3.3.1
  - python-dateutil 2.9.0.post0
  - pytz 2025.2
  - scikit-learn 1.8.0
  - scipy 1.17.0
  - seaborn 0.13.2
  - six 1.17.0
  - threadpoolctl 3.6.0
  - tzdata 2025.3

## Repository Structure

```struct
- docs/             - Documentation catalog.
- data/             - Directory for data.
  ├── reference/    - all needs references.
  ├── raw/          - Raw data.
  ├── intermediate/ - Intermediate data from all raw data sources.
  └── processed/    - Processed data.
- figures/          - Figures.
- src/              - Code sources for testing or trying analize data.
- report/           - Reports for showing this project.
```

## Data Sources

- [our-world-in-data](https://github.com/owid/energy-data) - Our World in Data — Energy Datasets github repo. (Uses like a submodule)
- [BP-energy-institute](https://www.energyinst.org/statistical-review) - Statistical Review of World Energy - saved as `.xlsx`

## Usage

### Reading analysis
- [In order to undertake reading analysis online without the necessity of compilation, it is recommended that the catalog file in the repository be utilised.](./Docs/README.md)

### Run pipelines

- Setup project:
  - Install python with required version.
  - Install all packages `pip install -r requirements.txt`
- Run Pipelines:
  - `python3.12 ./src/xx_pipeline_step/main.py`

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
