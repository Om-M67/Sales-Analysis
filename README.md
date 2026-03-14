# 🛒 Superstore Sales Analysis

An end-to-end exploratory data analysis (EDA) of the Superstore retail dataset using Python. This project uncovers revenue trends, regional performance, and product profitability to help businesses make data-driven decisions.

---

## 📌 Project Overview

Retail businesses generate enormous amounts of transactional data. This project analyzes the popular **Superstore Sales dataset** to answer key business questions:

- Which regions generate the most revenue?
- Which product categories and sub-categories are most profitable?
- How do sales trend over time?
- Who are the top customers by sales?

---

## 📁 Repository Structure

```
superstore-sales-analysis/
│
├── data/
│   └── Sample - Superstore.csv       # Raw dataset
│
├── charts/
│   ├── chart1_sales_by_region.png
│   ├── chart2_profit_by_category.png
│   ├── chart3_monthly_sales_trend.png
│   ├── chart4_profit_by_subcategory.png
│   └── chart5_top10_customers.png
│
├── superstore_analysis.py             # Main analysis script
├── requirements.txt                   # Python dependencies
└── README.md
```

---

## 📊 Dataset

- **Source:** [Kaggle – Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Records:** 9,994 orders
- **Time Range:** January 2014 – December 2017
- **Key Columns:** `Order Date`, `Region`, `Category`, `Sub-Category`, `Sales`, `Profit`, `Quantity`, `Discount`

---

## 🔧 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/superstore-sales-analysis.git
cd superstore-sales-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add the dataset
Download `Sample - Superstore.csv` from [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) and place it in the `data/` folder.

### 4. Run the analysis
```bash
python superstore_analysis.py
```

Charts will be saved to the `charts/` folder and key findings printed to the console.

---

## 📈 Key Findings

| Insight | Detail |
|---|---|
| 🏆 Top revenue region | **West** — $725,458 |
| 💰 Most profitable category | **Technology** — $145,455 profit |
| ⭐ Best sub-category | **Copiers** — $55,618 profit |
| 📉 Loss-making sub-category | **Tables** — ($17,725) loss |
| 📅 Peak sales month | **November 2017** |
| 👤 Top customer | **Sean Miller** — $25,043 |

### Regional Sales
The **West** leads in total revenue ($725K), followed closely by the **East** ($678K). The **Central** region underperforms relative to its geographic size and may warrant further investigation.

### Product Categories
**Technology** is the clear profit leader at $145K, while **Furniture** generates high revenue ($742K) but very low profit ($18K) — suggesting discounting or cost issues. **Tables** and **Bookcases** are actively losing money and should be reviewed.

### Monthly Trends
Sales show a consistent **end-of-year spike** each November–December, likely driven by holiday purchasing. This pattern repeats across all four years in the dataset.

---

## 📉 Charts

### Sales by Region
![Sales by Region](charts/chart1_sales_by_region.png)

### Profit by Category
![Profit by Category](charts/chart2_profit_by_category.png)

### Monthly Sales Trend
![Monthly Trend](charts/chart3_monthly_sales_trend.png)

### Profit by Sub-Category
![Sub-Category Profit](charts/chart4_profit_by_subcategory.png)

### Top 10 Customers
![Top Customers](charts/chart5_top10_customers.png)

---

## 🛠 Methods

1. **Data Cleaning** — checked for duplicates, missing values, and fixed date types using `pandas`
2. **Exploratory Analysis** — grouped and aggregated data using `groupby`, `sum`, and `sort_values`
3. **Visualization** — created bar charts and line charts using `matplotlib`
4. **Insight Generation** — summarized findings into actionable business conclusions

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| pandas | Data loading, cleaning, and analysis |
| matplotlib | Data visualization |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

Made with Python and curiosity. Feel free to fork, star ⭐, or open an issue!
