Automated Data Analysis & Reporting Tool (Python Automation)

A production-ready Python automation project that performs end-to-end data analysis on retail order data, generates insights, visualizations, and automated Excel reports with logging and error handling.

This project is designed to be job-ready for roles such as Data Analyst, Python Developer, Data Scientist (Fresher).

📌 Key Features

📊 Automated data cleaning and transformation

📈 Yearly sales trend visualization

💰 Monthly revenue analysis

📑 Automated Excel report generation

🪵 Logging & exception handling (production level)

🧩 Modular and scalable design

❌ No external API dependency (easy to run anywhere)

🗂️ Project Structure
automated-data-analysis/
│
├── data/
│   └── orders.csv
│
├── reports/
│   ├── retail_analysis_report.xlsx
│   └── yearly_sales.png
│
├── logs/
│   └── app.log
│
├── main.py
├── requirements.txt
└── README.md

📂 Dataset Description

Retail Orders Dataset

Columns used in analysis:

Order Date

List Price

Quantity

Category / Region / Segment

The dataset is manually downloaded and stored locally to avoid API dependency.

⚙️ Tech Stack

Python

Pandas – Data processing & aggregation

Matplotlib – Data visualization

OpenPyXL – Excel report automation

Logging – Application monitoring

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Ensure Folder Structure

Make sure orders.csv is placed inside the data/ folder.

3️⃣ Run Automation
python main.py

📊 Output Generated
📑 Excel Report

reports/retail_analysis_report.xlsx

Raw_Data – Cleaned dataset

Yearly_Sales – Aggregated yearly quantity

Monthly_Revenue – Monthly revenue trends

📈 Visualization

reports/yearly_sales.png

Bar chart showing yearly sales trend

🪵 Logs

logs/app.log

Execution details

Errors (if any)

Pipeline status

🧠 Business Logic Implemented

Revenue calculation:

revenue = quantity × list_price


Yearly aggregation using order date

Monthly revenue aggregation

Defensive programming to avoid runtime failures

🛠️ Error Handling & Logging

Handles missing or invalid dates

Prevents empty report generation

Logs every pipeline step

Graceful failure with meaningful error messages
