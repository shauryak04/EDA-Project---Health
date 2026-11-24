# Health Data – Exploratory Data Analysis

Explore patient health indicators (blood pressure, cholesterol, heart rate, temperature) and see how they vary by age, diabetic status, gender and city.

## Dataset

**File:** `data/Health.csv`

Key columns used:

- Age
- Gender
- City
- BloodPressure – stored as `Systolic/Diastolic` text (e.g. `120/80`)
- HeartRate
- Cholesterol
- Temperature
- Diabetic

## What the analysis does

1. Split `BloodPressure` into numeric `Systolic` and `Diastolic` columns
2. Inspect structure and summary statistics
3. Check for missing values and duplicate rows
4. Univariate analysis of categorical and numeric columns
5. Bivariate analysis and correlation of numeric features

## Visualisations

| Chart | Type |
|-------|------|
| Gender Distribution | Bar chart |
| Diabetic Proportion | Pie chart with percentages |
| City Distribution | Bar chart |
| Heart Rate Distribution | Histogram |
| Cholesterol Levels | Box plot to spot outliers |
| Age vs Heart Rate | Scatter plot |
| Cholesterol by Diabetic Status | Box plot |
| Average Temperature by City | Bar plot |
| Correlation Analysis | Heatmap of numeric features |

## Questions explored

- Do diabetic patients have higher cholesterol?
- Does heart rate change with age?
- Which health metrics are correlated with each other?

## Key insights

<!-- Run the script and write 3–5 findings here, e.g. "Customers in X had the highest ..." -->

- _Add your findings here_

## How to run

From the root of the repository:

```bash
pip install -r requirements.txt
python 02_health_eda/health_eda.py
```

Make sure `Health.csv` is in the `data/` folder. Each chart opens in a window; close it to see the next one.

## Tools

Python · pandas · matplotlib · seaborn

---
[← Back to all projects](../README.md)
