# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Total'] = df['Confirmed'] + df['Recovered'] + df['Deaths']

# Plot: Total cases over time
plt.figure(figsize=(10, 5))
daily_totals = df.groupby('Date')['Total'].sum()
plt.plot(daily_totals.index, daily_totals.values)
plt.title('Global Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot: Top 10 countries by total cases
country_totals = df.groupby('Country')['Total'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=country_totals.values, y=country_totals.index)
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()