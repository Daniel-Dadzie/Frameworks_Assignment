import streamlit as st
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

# Streamlit layout
st.title("COVID-19 Data Explorer")
st.write("Interactive dashboard using global COVID-19 data")

# Year range slider
year_range = st.slider("Select Year Range", 2020, 2022, (2020, 2021))
filtered_df = df[df['Year'].between(*year_range)]

# Line chart: Total cases over time
st.write("### Global Total Cases Over Time")
daily_totals = filtered_df.groupby('Date')['Total'].sum()
fig1, ax1 = plt.subplots()
ax1.plot(daily_totals.index, daily_totals.values)
ax1.set_xlabel("Date")
ax1.set_ylabel("Total Cases")
ax1.set_title("Global Total COVID-19 Cases")
st.pyplot(fig1)

# Bar chart: Top countries
st.write("### Top 10 Countries by Total Cases")
country_totals = filtered_df.groupby('Country')['Total'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=country_totals.values, y=country_totals.index, ax=ax2)
ax2.set_xlabel("Total Cases")
ax2.set_ylabel("Country")
ax2.set_title("Top 10 Countries")
st.pyplot(fig2)

# Show sample data
st.write("### Sample Data")
st.dataframe(filtered_df.head(10))