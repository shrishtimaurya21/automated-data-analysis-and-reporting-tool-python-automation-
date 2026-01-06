import os
import logging
import pandas as pd
import matplotlib.pyplot as plt


# BASE DIRECTORY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "orders.csv")
REPORT_PATH = os.path.join(BASE_DIR, "reports", "retail_analysis_report.xlsx")
CHART_PATH = os.path.join(BASE_DIR, "reports", "yearly_sales.png")
LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")


# LOGGING SETUP

os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "reports"), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

# DATA ANALYSIS
def analyze_data():
    try:
        logger.info("Reading dataset")

        df = pd.read_csv(DATA_PATH)

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Convert date column
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df = df.dropna(subset=["order_date"])

        # Revenue calculation
        df["revenue"] = df["quantity"] * df["list_price"]

        # Yearly sales (quantity)
        yearly_sales = (
            df.groupby(df["order_date"].dt.year)["quantity"]
            .sum()
            .reset_index()
            .rename(columns={"order_date": "year", "quantity": "total_quantity"})
        )

        # Monthly revenue
        monthly_revenue = (
            df.groupby(pd.Grouper(key="order_date", freq="ME"))["revenue"]
            .sum()
            .reset_index()
        )

        logger.info("Data analysis completed successfully")
        return df, yearly_sales, monthly_revenue

    except Exception as e:
        logger.error(f"Error during data analysis: {e}")
        raise


# VISUALIZATION

def create_visualization(yearly_sales):
    try:
        plt.figure(figsize=(8, 4))
        plt.bar(yearly_sales["year"], yearly_sales["total_quantity"])
        plt.title("Yearly Sales Trend")
        plt.xlabel("Year")
        plt.ylabel("Total Quantity")
        plt.tight_layout()
        plt.savefig(CHART_PATH)
        plt.close()

        logger.info("Yearly sales chart created successfully")

    except Exception as e:
        logger.error(f"Visualization error: {e}")
        raise



# REPORT GENERATION

def generate_report(df, yearly_sales, monthly_revenue):
    try:
        with pd.ExcelWriter(REPORT_PATH, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Raw_Data", index=False)
            yearly_sales.to_excel(writer, sheet_name="Yearly_Sales", index=False)
            monthly_revenue.to_excel(writer, sheet_name="Monthly_Revenue", index=False)

        logger.info("Excel report generated successfully")

    except Exception as e:
        logger.error(f"Report generation failed: {e}")
        raise


# MAIN PIPELINE

def main():
    try:
        logger.info("Automation pipeline started")

        df, yearly_sales, monthly_revenue = analyze_data()

        # Safety checks
        assert not df.empty, "Raw data is empty"
        assert not yearly_sales.empty, "Yearly sales is empty"
        assert not monthly_revenue.empty, "Monthly revenue is empty"

        create_visualization(yearly_sales)
        generate_report(df, yearly_sales, monthly_revenue)

        logger.info("Automation pipeline completed successfully")
        print("✅ Report & chart generated successfully!")

    except Exception as e:
        logger.critical(f"Pipeline failed: {e}")
        print("❌ Pipeline failed. Check logs/app.log")

if __name__ == "__main__":
    main()
