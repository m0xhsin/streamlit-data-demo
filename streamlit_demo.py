import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Interactive Data Presentation Demo", layout="wide")


st.title("🌟 Interactive Data Visualization Demo")
st.markdown("""
Welcome to a **Streamlit demo**!
This demo showcases:
- Interactive charts
- Dynamic data filtering
- Real-time calculations
- Fun widgets to engage the audience
- Beautiful images
""")


st.header("1️⃣ Explore an Image")
img_url = "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d"
st.image(img_url, caption="Beautiful scenery from Unsplash", width=700)  # updated from use_column_width


st.header("2️⃣ Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Visitors Today", "1,245", "+12%")
col2.metric("Revenue", "$8,432", "+8%")
col3.metric("Satisfaction", "89%", "+3%")


st.header("3️⃣ Interactive Data Table")
data = pd.DataFrame({
    "Country": ["Germany", "France", "India", "USA", "Brazil"],
    "Population (M)": [83, 67, 1391, 331, 213],
    "GDP (B$)": [3846, 2715, 2875, 22675, 1445]
})
selected_countries = st.multiselect("Select countries to display:", options=data["Country"], default=data["Country"])
filtered_data = data[data["Country"].isin(selected_countries)]
st.dataframe(filtered_data)


st.header("4️⃣ Population vs GDP")
# Simple bar chart using Streamlit
st.bar_chart(data.set_index("Country")[["Population (M)", "GDP (B$)"]])

st.header("5️⃣ Predict Revenue Growth")
growth = st.slider("Expected growth rate (%)", 0, 50, 10)
predicted_revenue = 8432 * (1 + growth/100)
st.metric("Predicted Revenue", f"${predicted_revenue:,.0f}", f"{growth}% growth")

st.header("6️⃣ Pick Your Favorite Country")
favorite = st.radio("Choose one:", options=data["Country"])
st.write(f"🌏 You selected **{favorite}**! Excellent choice!")


st.header("7️⃣ Progress Bar Simulation")
progress = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress.progress(i)
st.success("✅ Progress Complete!")


st.markdown("---")
st.markdown("Presented by **Mohsin Khan** | Streamlit Interactive Demo 🚀")
