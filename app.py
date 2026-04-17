import streamlit as st
import pandas as pd

st.title("🎓 CET Cutoff Analyzer (3 Years)")

# Load data
df = pd.read_csv("data.csv")

# Dropdown filters
college = st.selectbox("Select College", df["College"].unique())
course = st.selectbox("Select Course", df["Course"].unique())

# Filter data
filtered = df[(df["College"] == college) & (df["Course"] == course)]

# Sort and get last 3 years
result = filtered.sort_values(by="Year", ascending=False).head(3)

# Show result
st.subheader("📊 Last 3 Years Cutoff")
st.write(result)

# Download button
st.download_button("Download CSV", result.to_csv(index=False), "cutoff.csv")
