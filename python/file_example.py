# Flat file ETL example

import pandas as pd
from datetime import datetime as dt

data_path = "../data"
output_path = "../output"

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

        # TRANSFORM phase
        spent_per_order = []
        region_order = []
        category_order = []
        for index, row in orders_df.iterrows():
            amount_spent = products_df[products_df["ID"] == row["ProductID"]]["UnitPrice"] * row["Quantity"]
            # Selected unit price of the product based on it's ID, then multiplied by the quantity ordered
            spent_per_order.append(round(float(amount_spent.iloc[0]),2))
            # iloc used to convert series of single element, using only float() will result in a TypeError in the future
            region = customers_df[customers_df["ID"] == row["CustomerID"]]["Region"]
            # Selected region of the customer based on it's ID
            region_order.append(region.iloc[0])

            category = products_df[products_df["ID"] == row["ProductID"]]["Category"]
            # Selected category of the product based on it's ID
            category_order.append(category.iloc[0])
        
        # New dataframe
        new_transformed_df = pd.DataFrame({"region": region_order, "category": category_order, "total_spent": spent_per_order})
        print("New transformed dataframe:")
        print(new_transformed_df)
        
        region_spent = new_transformed_df.groupby("region").sum("total_spent")
        print("\n\nTotal $ spent by region:")
        print(region_spent)

        category_spent = new_transformed_df.groupby("category").sum("total_spent")
        print("\n\nTotal $ spent per category:")
        print(category_spent)

        # LOAD phase
        print("Writing 'spent_by_region.csv' file...")
        region_spent.to_csv(f"{output_path}/spent_by_region.csv")
        print("File created.")

        print("Writing 'spent_per_category.csv' file...")
        category_spent.to_csv(f"{output_path}/spent_per_category.csv")
        print("File created.")
    except Exception as e:
        # Exception error aliased as 'e' then formatted in the line below
        print(f"Error executing main script: {e}")

if __name__ == "__main__":
    print("Script started: ", dt.now())
    main()
    print("Script finished: ", dt.now())