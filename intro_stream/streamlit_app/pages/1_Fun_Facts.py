import streamlit as st
import constants as c

st.set_page_config(
    page_title="1. Fun Facts",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)


margin_r, body, margin_l = st.columns([0.4, 3, 0.4])


with body:
    c.menu()

    st.header("👨‍👩‍👧 Family", divider='rainbow')
    col1, col2, col3 = st.columns([1.3, 0.2, 1])
    with col1:
        st.markdown(f"###### 👨‍👩‍👧 Family: {c.facts['family']}")    

    with col3:
        st.image("images/disney.jpeg", width=360)

    st.subheader("🌍 Countries", divider='rainbow')
    col1, col2, col3 = st.columns([1.3, 0.2, 1])
    with col1:
        st.markdown(f"###### 🌍 Countries: {c.facts['countries']}")
