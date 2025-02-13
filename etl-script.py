import pandas as pd

# Path to the folder where the CSV files are stored
folder_path = "C:/Users/HP/Desktop/BIG-data-project/"

# Load datasets into Pandas DataFrames
customers_df = pd.read_csv(folder_path + "olist_customers_dataset.csv")
geolocation_df = pd.read_csv(folder_path + "olist_geolocation_dataset.csv")
order_items_df = pd.read_csv(folder_path + "olist_order_items_dataset.csv")
order_payments_df = pd.read_csv(folder_path + "olist_order_payments_dataset.csv")
order_reviews_df = pd.read_csv(folder_path + "olist_order_reviews_dataset.csv")
orders_df = pd.read_csv(folder_path + "olist_orders_dataset.csv")
products_df = pd.read_csv(folder_path + "olist_products_dataset.csv")
sellers_df = pd.read_csv(folder_path + "olist_sellers_dataset.csv")
product_category_df = pd.read_csv(folder_path + "product_category_name_translation.csv")

# Show column info and first few rows for each dataset
datasets = {
    "Customers Dataset": customers_df,
    "Geolocation Dataset": geolocation_df,
    "Order Items Dataset": order_items_df,
    "Order Payments Dataset": order_payments_df,
    "Order Reviews Dataset": order_reviews_df,
    "Orders Dataset": orders_df,
    "Products Dataset": products_df,
    "Sellers Dataset": sellers_df,
    "Product Category Dataset": product_category_df,
}

for name, df in datasets.items():
    print(f"\n{name}:")
    print(df.info())  
    print(df.head())

# Count total rows in all datasets
total_rows = sum(df.shape[0] for df in datasets.values())
print(f"\nTotal number of rows across all datasets: {total_rows}")
