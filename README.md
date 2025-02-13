
## Prepared By:
Seyfedin Shukur
ID Number: addbu/046/14D

# E-Commerce Data Analysis - Brazilian E-Commerce (Olist)

This project analyzes the Brazilian e-commerce (Olist) dataset to extract insights into customer behavior, product trends, and seller performance. It involves data cleaning, transformation, and loading the cleaned data into PostgreSQL for further analysis.

# Tools & Technologies
PostgreSQL: Relational database for data storage.
Pandas: Data processing library.
SQLAlchemy: PostgreSQL connection.
Power BI: For data visualization.
VS Code: Code editor.

## Dataset Overview

- **Dataset Name**: Brazilian E-Commerce Data (Olist)
- **Source**: Kaggle
- **Size**: 1.5+ million rows across multiple CSV files

## Steps & Code

1. **Load Data**: Import data from CSV files.
2. **Clean Data**: Remove duplicates, handle missing values, and format data types.
3. **Load to PostgreSQL**: Store cleaned data into a PostgreSQL database for analysis.

```python
## Full code example
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Step 1: Load Data
orders = pd.read_csv('orders.csv')

# Step 2: Data Cleaning
orders_cleaned = orders.drop_duplicates()
orders_cleaned['order_purchase_timestamp'] = pd.to_datetime(orders_cleaned['order_purchase_timestamp'])
orders_cleaned.fillna(method='ffill', inplace=True)

# Step 3: Database Connection
db_params = {
    'dbname': 'big_data_project',
    'user': 'postgres',
    'password': 'sigma@boy1',
    'host': 'localhost',
    'port': '5432'
}
conn = psycopg2.connect(**db_params)

# Step 4: Create SQLAlchemy engine to load data into PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:sigma@boy1@localhost:5432/postgres')

# Load cleaned data into PostgreSQL
orders_cleaned.to_sql('orders', engine, if_exists='replace', index=False)

# Step 5: Verify Data Load
query = "SELECT * FROM orders LIMIT 5"
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()
