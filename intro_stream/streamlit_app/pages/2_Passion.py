import streamlit as st
import constants as c

st.set_page_config(
    page_title="2. Passion",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

margin_r, body, margin_l = st.columns([0.4, 3, 0.4])


with body:
    c.menu()

    st.subheader("🍰 Cakes and Cookies", divider='rainbow')
    col1, col2, col3 = st.columns([1.3, 0.2, 1])
    with col1:
        st.markdown(f"###### {c.passions['cakes']}")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🏊‍♀️ Swimming", divider='rainbow')
    col1, col2, col3 = st.columns([1.3, 0.2, 1])
    with col1:
        st.markdown(f"###### {c.passions['swimming']}")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🌱 Renewable Energy", divider='rainbow')    
    st.markdown(f"###### {c.passions['renewable_energy']}")
    st.markdown(f" - {c.passions['project']}")
    st.markdown(f" - {c.passions['bess']}")
