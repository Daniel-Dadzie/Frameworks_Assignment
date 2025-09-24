# Import pandas for data handling
import pandas as pd

# Load a sample COVID-19 dataset from GitHub
url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(url)

# Show the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Show dataset dimensions
print("\nDataset dimensions (rows, columns):")
print(df.shape)

# Show column data types
print("\nColumn data types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())