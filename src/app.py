import pandas as pd

data = pd.read_csv("data/ecommerce_sales_data.csv")
shape = data.shape
print("Shape:")
print(shape)
print("Preview: \n")
print(data.head())

print("data types:")
print(data.dtypes)
