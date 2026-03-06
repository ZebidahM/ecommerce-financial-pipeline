# E-Commerce Sales Data Analysis (2009–2011)

Exploratory data analysis of a multi-year e-commerce transaction dataset using Python and Jupyter Notebook. The project covers data cleaning, feature engineering, revenue calculation, and visualization of sales trends.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Tools and Libraries](#tools-and-libraries)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Key Findings](#key-findings)
- [How to Run](#how-to-run)

---

## Project Overview

The dataset contains e-commerce transactions from 2009 to 2011, split across two CSV files. The goal was to merge, clean, and analyze the data to uncover insights around product performance, geographic sales distribution, and revenue trends over time.

---

## Tools and Libraries

- Python 3
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Structure

```
ecommerce-sales-analysis/
│
├── data/
│   ├── raw/
│   │   ├── Year 2009_2010.csv      # Original dataset: 2009 to 2010
│   │   └── Year 2010_2011.csv      # Original dataset: 2010 to 2011
│   │
│   └── cleaned/
│       └── transactions_cleaned.csv        # Merged and cleaned dataset
│
├── notebooks/
│   └── E-commerce Global Sales Analysis.ipynb            # Main analysis notebook
│
├── visuals/
│   ├── monthly_sales_trend.png             # Monthly revenue chart
│   └── top_countries_by_revenue.png        # Geographic sales breakdown
│
├── README.md
└── requirements.txt                        # Python dependencies
```

### Data Folder Explained

**raw/** — Contains the original, unmodified CSV files exactly as downloaded. These are never edited. If anything goes wrong during cleaning, you can always come back to these.

**cleaned/** — Contains the processed dataset after the following steps were applied:
- Removed rows with missing customer IDs
- Filtered out cancelled transactions
- Converted InvoiceDate to datetime format
- Added Year and Month columns
- Added a Revenue column (Quantity x Price)

---

## Workflow

1. Imported pandas, numpy, matplotlib, and seaborn
2. Loaded both raw CSV files
3. Merged them into a single dataframe using glob and pandas
4. Reviewed structure using `.shape`, `.columns`, and `.info()`
5. Identified and handled missing values
6. Removed rows with missing customer IDs
7. Filtered out cancelled transactions
8. Converted InvoiceDate to datetime format
9. Validated dates using `errors="coerce"`
10. Extracted Year and Month as new columns
11. Calculated revenue per transaction
12. Analyzed top products by units sold
13. Grouped transactions by country to assess geographic revenue
14. Visualized monthly sales trends and top revenue regions
15. Exported cleaned dataset to `data/cleaned/`

---

## Key Findings

- **Top products** by quantity sold were concentrated in a small number of SKUs
- **The UK** accounted for the largest share of total revenue
- **Sales peaked** during certain months, suggesting seasonal buying patterns


---

## How to Run

1. Clone the repository
```
git clone https://github.com/ZebidahM/ecommerce-sales-analysis.git
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Open the notebook
```
jupyter notebook notebooks/E-commerce Global Sales Analysis.ipynb
```

---

## Data Source

The dataset used in this project is publicly available on [Kaggle](https://www.kaggle.com/) or the [UCI Machine Learning Repository](https://archive.ics.uci.edu/).
