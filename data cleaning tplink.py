import pandas as pd
import numpy as np

df = pd.read_csv('TPLink.csv')

## Remove unwanted columns
# Remove first column 'volume-price-tag' if it exists
if 'volume-price-tag' in df.columns:
    df = df.drop(columns=['volume-price-tag'])

## price Cleaning
# Clean the 'price' column by removing dollar signs and commas, then convert to float
df['price'] = df['price'].replace('[RM,\s]', '', regex=True).astype(float)

## prod-weight Cleaning
# Clean the 'prod-weight' column by removing 'Weight:' and any non-numeric characters, then convert to float
df['prod-weight'] = df['prod-weight'].replace('Weight:\s*', '', regex=True)
df['prod-weight'] = df['prod-weight'].replace('[kg,\s]', '', regex=True).astype(float)
df['prod-weight'] = df['prod-weight'].fillna(0) 

## in-stock Cleaning
# Clean 'in-stock' column by replacing 'In stock' with 1 and 'Out of stock' with 0
df['in-stock'] = df['in-stock'].replace({'In Stock': 1, 'Out of Stock': 0})
# Convert 'in-stock' NaN values to 1 and ensure it's an integer type
df['in-stock'] = df['in-stock'].fillna(1).astype(int)
# Convert 'in-stock' to numeric, coercing errors to NaN
df['in-stock'] = pd.to_numeric(df['in-stock'], errors='coerce')


# Export the cleaned DataFrame to a new CSV file
df.to_csv('TPLink_cleaned.csv', index=False)
print("Cleaned data saved to 'TPLink_cleaned.csv'")



# print(df.shape)
# print(df.info())
# print(df.head())