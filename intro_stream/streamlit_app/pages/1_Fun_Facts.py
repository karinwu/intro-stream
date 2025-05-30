import streamlit as st

st.set_page_config(
    page_title="1. Fun Facts",
    page_icon="🎉",
    layout="wide"
)

st.header("Fun Facts")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("👨‍👩‍👧 Family")
    st.write("I have a wonderful family of four.")
with col2:
    st.subheader("🌍 Countries")
    st.write("I've visited 10+ countries!")
with col3:
    st.subheader("🏆 Achievement")
    st.write("Won a regional baking competition.")
