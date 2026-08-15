import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Sales": [75000, 50000, 30000, 15000, 10000]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Highest Sales:", df["Sales"].max())
