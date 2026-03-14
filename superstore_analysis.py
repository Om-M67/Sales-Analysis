"""
Superstore Sales Analysis
=========================
Covers:
  1. Data loading & cleaning
  2. Exploratory analysis (sales by region, profit by category, monthly trends)
  3. Visualizations saved as PNG files
  4. Summary of key findings printed to console
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings("ignore")

# ── 0. CONFIG ────────────────────────────────────────────────────────────────
FILE_PATH = "Sample - Superstore.csv"   # adjust path if needed
OUTPUT_DIR = "."                         # folder where chart PNGs are saved

COLORS = {
    "blue":   "#4C72B0",
    "green":  "#55A868",
    "orange": "#C44E52",
    "purple": "#8172B2",
    "teal":   "#64B5CD",
}
PALETTE = list(COLORS.values())

plt.rcParams.update({
    "figure.dpi": 150,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 11,
})

# ── 1. LOAD & CLEAN ──────────────────────────────────────────────────────────
print("=" * 60)
print("SUPERSTORE SALES ANALYSIS")
print("=" * 60)

df = pd.read_csv(FILE_PATH, encoding="latin-1")

print(f"\n[1] Raw dataset shape: {df.shape}")

# Parse dates
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=False)
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  dayfirst=False)

# Check & drop duplicates
dupes = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"    Duplicate rows removed : {dupes}")

# Check missing values
missing = df.isnull().sum()
missing = missing[missing > 0]
if missing.empty:
    print("    Missing values         : none")
else:
    print(f"    Missing values:\n{missing}")

# Derived columns
df["Year"]       = df["Order Date"].dt.year
df["Month"]      = df["Order Date"].dt.to_period("M")
df["Profit Margin (%)"] = (df["Profit"] / df["Sales"] * 100).round(2)

print(f"\n    Date range : {df['Order Date'].min().date()}  →  {df['Order Date'].max().date()}")
print(f"    Orders     : {df['Order ID'].nunique():,}")
print(f"    Customers  : {df['Customer ID'].nunique():,}")
print(f"    Products   : {df['Product ID'].nunique():,}")

# ── 2. EXPLORATORY ANALYSIS ──────────────────────────────────────────────────
print("\n[2] Exploratory Analysis")

# 2a. Sales & Profit by Region
region = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
    .round(2)
)
print("\n  Sales & Profit by Region:")
print(region.to_string())

# 2b. Profit by Category
category = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .sort_values("Profit", ascending=False)
    .round(2)
)
print("\n  Sales & Profit by Category:")
print(category.to_string())

# 2c. Profit by Sub-Category (top 10)
sub_cat = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
print("\n  Top 5 / Bottom 5 Sub-Categories by Profit:")
print(pd.concat([sub_cat.head(5), sub_cat.tail(5)]).to_string())

# 2d. Monthly Sales Trend
monthly = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)
monthly["Month_dt"] = monthly["Month"].dt.to_timestamp()

# 2e. Top 10 Customers
top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# ── 3. VISUALISATIONS ────────────────────────────────────────────────────────
print("\n[3] Creating charts …")

def save(fig, name):
    path = f"{OUTPUT_DIR}/{name}"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"    Saved → {path}")


# Chart 1 – Sales by Region (horizontal bar)
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(region.index, region["Sales"], color=PALETTE[:len(region)])
ax.bar_label(bars, labels=[f"${v/1e6:.2f}M" for v in region["Sales"]], padding=5)
ax.set_xlabel("Total Sales (USD)")
ax.set_title("Total Sales by Region", fontweight="bold", pad=12)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
ax.set_xlim(0, region["Sales"].max() * 1.18)
save(fig, "chart1_sales_by_region.png")


# Chart 2 – Profit by Category (bar)
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(category.index, category["Profit"],
              color=[COLORS["green"], COLORS["blue"], COLORS["orange"]])
ax.bar_label(bars, labels=[f"${v/1e3:.0f}K" for v in category["Profit"]], padding=4)
ax.set_ylabel("Total Profit (USD)")
ax.set_title("Total Profit by Product Category", fontweight="bold", pad=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
ax.set_ylim(0, category["Profit"].max() * 1.18)
save(fig, "chart2_profit_by_category.png")


# Chart 3 – Monthly Sales Trend (line)
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(monthly["Month_dt"], monthly["Sales"],
        color=COLORS["blue"], linewidth=2, marker="o", markersize=3)
ax.fill_between(monthly["Month_dt"], monthly["Sales"], alpha=0.12, color=COLORS["blue"])
ax.set_xlabel("Month")
ax.set_ylabel("Sales (USD)")
ax.set_title("Monthly Sales Trend", fontweight="bold", pad=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
fig.autofmt_xdate(rotation=45)
save(fig, "chart3_monthly_sales_trend.png")


# Chart 4 – Sub-Category Profit (horizontal bar, colour-coded +/-)
fig, ax = plt.subplots(figsize=(9, 7))
colors = [COLORS["green"] if v >= 0 else COLORS["orange"] for v in sub_cat.values]
bars = ax.barh(sub_cat.index, sub_cat.values, color=colors)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel("Total Profit (USD)")
ax.set_title("Profit by Sub-Category", fontweight="bold", pad=12)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
save(fig, "chart4_profit_by_subcategory.png")


# Chart 5 – Top 10 Customers by Sales
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_customers.index[::-1], top_customers.values[::-1],
               color=COLORS["teal"])
ax.bar_label(bars, labels=[f"${v/1e3:.1f}K" for v in top_customers.values[::-1]], padding=4)
ax.set_xlabel("Total Sales (USD)")
ax.set_title("Top 10 Customers by Sales", fontweight="bold", pad=12)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
ax.set_xlim(0, top_customers.max() * 1.2)
save(fig, "chart5_top10_customers.png")


# ── 4. KEY FINDINGS ──────────────────────────────────────────────────────────
top_region      = region["Sales"].idxmax()
top_region_val  = region["Sales"].max()
top_cat_profit  = category["Profit"].idxmax()
worst_subcat    = sub_cat.idxmin()
best_subcat     = sub_cat.idxmax()
peak_month      = monthly.loc[monthly["Sales"].idxmax(), "Month_dt"].strftime("%B %Y")
best_customer   = top_customers.idxmax()

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)
print(f"  • Top revenue region    : {top_region} (${top_region_val:,.0f})")
print(f"  • Most profitable cat.  : {top_cat_profit}")
print(f"  • Best sub-category     : {best_subcat} (${sub_cat.max():,.0f} profit)")
print(f"  • Loss-making sub-cat.  : {worst_subcat} (${sub_cat.min():,.0f} profit)")
print(f"  • Peak sales month      : {peak_month}")
print(f"  • Top customer by sales : {best_customer} (${top_customers.max():,.0f})")
print("\nAll charts saved as PNG files in the current directory.")
print("=" * 60)
