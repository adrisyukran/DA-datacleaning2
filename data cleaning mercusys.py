import pandas as pd
import numpy as np

df = pd.read_csv('Mercusys.csv')


# Clean the 'price' column by removing dollar signs and commas, then convert to float
df['price'] = df['price'].replace('[RM,\s]', '', regex=True).astype(float)

# Clean the 'prod-weight' column by removing 'Weight:' and any non-numeric characters, then convert to float
df['prod-weight'] = df['prod-weight'].replace('Weight:\s*', '', regex=True)
df['prod-weight'] = df['prod-weight'].replace('[kg,\s]', '', regex=True).astype(float)



# print(df.shape)
# print(df.info())
print(df.head())