import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="UNCA Dashboard", layout="wide")
st.title("🌿 UN-Climate Action: Mini Dashboard")
st.markdown("Demo data — replace with your CSV later.")

# Sample demo data
data = {
    "District": ["Bajaur","Khyber","Mohmand"],
    "Afforestation (ha)": [1200,1500,800],
    "ANR (ha)": [700,900,650],
    "Survival (%)":[85,80,82]
}
df = pd.DataFrame(data)

# Sidebar filter
districts = st.sidebar.multiselect("Choose District(s):", df["District"].unique(), default=df["District"].unique())
df = df[df["District"].isin(districts)]

# Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Afforestation (ha)", f"{df['Afforestation (ha)'].sum():,}")
c2.metric("ANR (ha)", f"{df['ANR (ha)'].sum():,}")
c3.metric("Avg Survival", f"{df['Survival (%)'].mean():.1f}%")

# Chart
fig = px.bar(df, x="District", y=["Afforestation (ha)","ANR (ha)"], barmode="group")
st.plotly_chart(fig, use_container_width=True)
