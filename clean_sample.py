# Import pandas
import pandas as pd

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(url)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract 'Year' and 'Month' from the date
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Create a new column for total cases
df['Total'] = df['Confirmed'] + df['Recovered'] + df['Deaths']

# Show a preview of the cleaned data
print("Cleaned data preview:")
print(df.head())

# Show summary of new columns
print("\nNew columns added:")
print(df[['Date', 'Year', 'Month', 'Total']].head())