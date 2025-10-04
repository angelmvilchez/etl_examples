# Flat file ETL example

import pandas as pd

data_path = "../data"

def main():
    try:
        # EXTRACT phase
        print("Reading 'customers.csv'...")
        customers_df = pd.read_csv(f"{data_path}/customers.csv")
        print("Customers dataset read correctly.")
        print(customers_df, end="\n\n")

        print("Reading 'orders.csv'...")
        orders_df = pd.read_csv(f"{data_path}/orders.csv")
        print("Orders dataset read correctly.")
        print(orders_df, end="\n\n")

        print("Reading 'products.csv'...")
        products_df = pd.read_csv(f"{data_path}/products.csv")
        print("Products dataset read correctly.")
        print(products_df, end="\n\n")
    except Exception as e:
        # Exception error aliased as 'e' then formatted in the line below
        print(f"Error executing main script: {e}")

if __name__ == "__main__":
    main()