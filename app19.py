import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
cleaned_data = pd.read_csv('metadata.csv', low_memory=False, nrows=100)
cleaned_data['publish_time'] = pd.to_datetime(cleaned_data['publish_time'], errors='coerce')
cleaned_data['year'] = cleaned_data['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata interactively.")

# --- Dynamic Year Slider Setup ---
if cleaned_data['year'].notna().sum() > 0:
    years = sorted(cleaned_data['year'].dropna().unique())
    min_year, max_year = int(min(years)), int(max(years))

    st.sidebar.header("Filters")
    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    filtered_df = cleaned_data[
        (cleaned_data['year'] >= year_range[0]) & (cleaned_data['year'] <= year_range[1])
    ]

    if filtered_df.empty:
        st.warning("⚠️ No data found for the selected year range. Try expanding the range.")
    else:
        # --- Visualizations ---
        st.subheader("📊 Publications by Year")
        year_counts = filtered_df['year'].value_counts().sort_index()
        fig, ax = plt.subplots()
        ax.bar(year_counts.index, year_counts.values)
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Publications")
        st.pyplot(fig)

        st.subheader("🏛️ Top Journals")
        if 'journal' in filtered_df.columns:
            top_journals = filtered_df['journal'].value_counts().head(10)
            st.bar_chart(top_journals)
        else:
            st.info("No 'journal' column found in the dataset.")

        st.subheader("☁️ Word Cloud of Titles")
        titles = " ".join(filtered_df['title'].dropna().astype(str))
        if titles.strip():
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
            st.image(wordcloud.to_array())
        else:
            st.warning("No titles available for the selected range.")

        st.subheader("📋 Sample Data")
        st.dataframe(filtered_df.head(20))
else:
    st.error("❌ No valid publication years found in the dataset.")
