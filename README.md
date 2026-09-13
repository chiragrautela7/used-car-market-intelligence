# Used Car Market & Pricing Intelligence

## Objective
Analyze used-car listings to identify pricing drivers, depreciation patterns, customer preferences, market segments, and potential pricing opportunities.

## Important dataset note
The included dataset is synthetic but realistic practice data. It intentionally contains missing values and duplicates so the cleaning workflow can be demonstrated. Do not present it as real market data.

## Workflow
Business Problem → Data Audit → Cleaning → Feature Engineering → EDA → Business Questions → Insights → Recommendations

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter

## Structure
- `data/raw/used_cars_raw.csv` — raw practice data
- `data/cleaned/used_cars_cleaned.csv` — cleaned + engineered data
- `src/clean_data.py` — reproducible cleaning script
- `notebooks/used_car_market_analysis.ipynb` — complete analysis notebook
- `reports/business_report.md` — report template
- `requirements.txt` — dependencies

## How to run
```bash
pip install -r requirements.txt
cd src
python clean_data.py
```
Then open the notebook and run all cells.

## Portfolio rule
Every conclusion should follow **Observation → Business Meaning → Recommendation** and must be based on the actual notebook output.
