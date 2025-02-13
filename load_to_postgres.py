import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import urllib.parse

# Database connection parameters
db_host = "localhost"
db_port = "5432"
db_name = "big_data_project"
db_user = "postgres"
db_password = "sigma@boy1"

# URL encode password to avoid errors with special characters
encoded_password = urllib.parse.quote(db_password)

# PostgreSQL connection string
connection_string = f"postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"

# Folder path containing CSV files
folder_path = "C:/Users/HP/Desktop/BIG-data-project/"

# List of datasets and their CSV filenames
datasets = {
    "customers": "cleaned_customers.csv",
    "geolocation": "cleaned_geolocation.csv",
    "order_items": "cleaned_order_items.csv",
    "order_payments": "cleaned_order_payments.csv",
    "order_reviews": "cleaned_order_reviews.csv",
    "orders": "cleaned_orders.csv",
    "products": "cleaned_products.csv",
    "sellers": "cleaned_sellers.csv",
    "product_category": "cleaned_product_category.csv"
}

# ✅ Step 1: Test Database Connection
try:
    connection = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
    )
    print(f"✅ Connected to database '{db_name}' successfully!")
    connection.close()
except Exception as e:
    print(f" Error connecting to database: {e}")
    exit()  # Stop script if connection fails

# ✅ Step 2: Load Data into PostgreSQL
try:
    # Create SQLAlchemy engine
    engine = create_engine(connection_string)

    for table_name, file_name in datasets.items():
        file_path = folder_path + file_name
        try:
            df = pd.read_csv(file_path)  # Read CSV file
            df.to_sql(table_name, engine, if_exists="replace", index=False, method="multi")  # Load into PostgreSQL
            print(f"✅ '{table_name}' table inserted successfully!")
        except Exception as e:
            print(f" Error loading '{table_name}': {e}")

    print("\n✅ All datasets have been loaded into PostgreSQL!")

except Exception as e:
    print(f" Error loading data: {e}")

# ✅ Step 3: Display First 5 Rows from Each Table
try:
    engine = create_engine(connection_string)
    connection = engine.connect()

    for table_name in datasets.keys():
        print(f"\n First 5 rows from '{table_name}':")
        query = f"SELECT * FROM {table_name} LIMIT 5;"
        df = pd.read_sql(query, connection)
        print(df)

    connection.close()

except Exception as e:
    print(f" Error fetching data: {e}")
