import streamlit as st

st.set_page_config(
    page_title="2. Passion",
    page_icon="❤️",
    layout="wide"
)

st.header("My Passions")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🍰 Cake")
    st.write("I love baking and decorating cakes.")
with col2:
    st.subheader("🏊‍♀️ Swimming")
    st.write("Swimming keeps me active and refreshed.")
with col3:
    st.subheader("🌱 Renewable Energy")
    st.write("I'm passionate about sustainable energy solutions.")
