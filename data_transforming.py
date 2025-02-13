import pandas as pd

# Define the folder path where the CSV files are stored
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

# ------------------------- Data Cleaning -------------------------

# Drop rows with missing values
customers_df.dropna(inplace=True)
geolocation_df.dropna(inplace=True)
order_items_df.dropna(inplace=True)
order_payments_df.dropna(inplace=True)
order_reviews_df.dropna(inplace=True)
orders_df.dropna(inplace=True)
products_df.dropna(inplace=True)
sellers_df.dropna(inplace=True)
product_category_df.dropna(inplace=True)

# Remove duplicate rows
customers_df.drop_duplicates(inplace=True)
geolocation_df.drop_duplicates(inplace=True)
order_items_df.drop_duplicates(inplace=True)
order_payments_df.drop_duplicates(inplace=True)
order_reviews_df.drop_duplicates(inplace=True)
orders_df.drop_duplicates(inplace=True)
products_df.drop_duplicates(inplace=True)
sellers_df.drop_duplicates(inplace=True)
product_category_df.drop_duplicates(inplace=True)

# Convert date columns to datetime format
date_columns = [
    'order_purchase_timestamp', 'order_approved_at',
    'order_delivered_carrier_date', 'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_columns:
    if col in orders_df.columns:
        orders_df[col] = pd.to_datetime(orders_df[col], errors='coerce')

# Convert numerical columns to appropriate types
numeric_columns = ['price', 'freight_value', 'payment_value']
for col in numeric_columns:
    if col in order_items_df.columns:
        order_items_df[col] = pd.to_numeric(order_items_df[col], errors='coerce')
    if col in order_payments_df.columns:
        order_payments_df[col] = pd.to_numeric(order_payments_df[col], errors='coerce')

# ------------------------- Save Cleaned Data -------------------------

# Save cleaned data for PostgreSQL storage
customers_df.to_csv(folder_path + "cleaned_customers.csv", index=False)
geolocation_df.to_csv(folder_path + "cleaned_geolocation.csv", index=False)
order_items_df.to_csv(folder_path + "cleaned_order_items.csv", index=False)
order_payments_df.to_csv(folder_path + "cleaned_order_payments.csv", index=False)
order_reviews_df.to_csv(folder_path + "cleaned_order_reviews.csv", index=False)
orders_df.to_csv(folder_path + "cleaned_orders.csv", index=False)
products_df.to_csv(folder_path + "cleaned_products.csv", index=False)
sellers_df.to_csv(folder_path + "cleaned_sellers.csv", index=False)
product_category_df.to_csv(folder_path + "cleaned_product_category.csv", index=False)

# ------------------------- Display Sample Data & Total Rows -------------------------

datasets = {
    "Customers": customers_df,
    "Geolocation": geolocation_df,
    "Order Items": order_items_df,
    "Order Payments": order_payments_df,
    "Order Reviews": order_reviews_df,
    "Orders": orders_df,
    "Products": products_df,
    "Sellers": sellers_df,
    "Product Category": product_category_df
}

total_rows = 0
print("\n Data Overview After Cleaning & Transformation:")
for name, df in datasets.items():
    row_count = df.shape[0]
    total_rows += row_count
    print(f"\n🔹 {name} Dataset - Total Rows: {row_count}")
    print(df.head())  # Show first 5 sample rows

print(f"\n Total Rows Across All Cleaned Datasets: {total_rows}")
print(" Data Cleaning & Transformation Completed Successfully!")
