import pandas as pd
def analyze_gold_sales(file):
    df = pd.read_csv(file)
    print("\n===== DATA PREVIEW =====")
    print(df.head())
    print("\n===== BASIC INFO =====")
    df.info()
    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())
    print("\n===== MEAN =====")
    print(df.mean(numeric_only=True))
    print("\n===== MEDIAN =====")
    print(df.median(numeric_only=True))
    print("\n===== VARIANCE =====")
    print(df.var(numeric_only=True))
    print("\n===== STANDARD DEVIATION =====")
    print(df.std(numeric_only=True))
    if "Brand" in df.columns and "Total Revenue" in df.columns:
        print("\n===== BRAND-WISE TOTAL SALES =====")
        brand_sales = df.groupby("Brand")["Total Revenue"].sum()
        print(brand_sales)
    else:
        print("\nBrand or Total Revenue column not found!")
    if "Year" in df.columns and "Grams Sold" in df.columns:
        print("\n===== YEAR-WISE GOLD SOLD (GRAMS) =====")
        yearly_sales = df.groupby("Year")["Grams Sold"].sum()
        print(yearly_sales)
    else:
        print("\nYear or Grams Sold column not found!")
if __name__ == "__main__":
    file = input("Enter Gold Sales CSV file path: ")
    analyze_gold_sales(file)
