# E-Commerce Data Analysis - Brazilian E-Commerce (Olist)

This project analyzes the Brazilian e-commerce (Olist) dataset to extract insights into customer behavior, product trends, and seller performance. It involves data cleaning, transformation, and loading the cleaned data into PostgreSQL for further analysis.

## Dataset Overview
- **Dataset Name**: Brazilian E-Commerce Data (Olist)
- **Source**: Kaggle
- **Size**: 1.5+ million rows across multiple CSV files
- **Key Files**: 
    - `orders.csv`, `order_items.csv`, `products.csv`, `customers.csv`, `reviews.csv`, `sellers.csv`, `payment.csv`

## Steps & Code

1. **Load Data**: Import data from CSV files.
2. **Clean Data**: Remove duplicates, handle missing values, and format data types.
3. **Load to PostgreSQL**: Store cleaned data into a PostgreSQL database for analysis.

### Full Code Example:

```python
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
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}
conn = psycopg2.connect(**db_params)

# Step 4: Create SQLAlchemy engine to load data into PostgreSQL
engine = create_engine('postgresql+psycopg2://your_username:your_password@localhost:5432/your_dbname')

# Load cleaned data into PostgreSQL
orders_cleaned.to_sql('orders', engine, if_exists='replace', index=False)

# Step 5: Verify Data Load
query = "SELECT * FROM orders LIMIT 5"
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()
