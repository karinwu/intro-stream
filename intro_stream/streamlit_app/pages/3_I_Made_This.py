import streamlit as st
import constants as c

st.set_page_config(
    page_title="3. I Made This",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state="collapsed"
)


margin_r, body, margin_l = st.columns([0.4, 3, 0.4])


with body:
    c.menu()

    st.header("🍰 Cakes and cookies I've Made")


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(
            "images/berry_cake.jpeg",
            caption="Berry Cake",
            use_container_width=True
        )
        st.image(
            "images/christmas_cookies.jpeg",
            caption="Christmas Cookies",
            use_container_width=True
        )
    with col2:
        st.image(
            "images/thomas_cake.jpeg",
            caption="Thomas Cake",
            use_container_width=True
        )
        st.image(
            "images/cupcakes.jpeg",
            caption="Cupcakes",
            use_container_width=True
        )
    with col3:
        st.image(
            "images/chocolate_cake.jpeg",
            caption="Chocolate Cake",
            use_container_width=True
        )
        st.image(
            "images/snowman_cookies.jpeg",
            caption="Snowman Cookies",
            use_container_width=True
        )
    with col4:
        st.image(
            "images/blueberry_cake.jpeg",
            caption="Blue Berry Cake",
            use_container_width=True
        )
        st.image(
            "images/trees.jpeg",
            caption="Christmas Tree",
            use_container_width=True
        )

    st.header("Models I've Made",  divider='rainbow')

    st.markdown(
        '<h3 style="color:green;">🧠 Temporal GNN</h3>',
        unsafe_allow_html=True
    )
    st.subheader("What is it?")
    st.markdown(c.models['GNN'])
    st.subheader("Who is it for?")
    st.markdown(c.models['GNN_audience'])
    st.subheader("Why is it relevant?")
    st.markdown(c.models['GNN_relevance'])

    st.link_button(
        "Go to Code",
        c.models['GNN_code'])
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<h3 style="color:green;">🤖 LLM</h3>',
        unsafe_allow_html=True
    )

    st.subheader("What is it?")
    st.markdown(c.models['LLM'])
    st.subheader("Who is it for?")
    st.markdown(c.models['LLM_audience'])
    st.subheader("Why is it relevant?")
    st.markdown(
        c.models['LLM_relevance'])

    st.link_button(
        "Go to Code",
        c.models['LLM_code'],
    )

    st.markdown("<br>", unsafe_allow_html=True)    
    st.markdown(
        '<h3 style="color:green;">📊 MLOps</h3>',
        unsafe_allow_html=True
    )
    st.subheader("What is it?")
    st.markdown(c.models['MLOps'])
    st.subheader("Who is it for?")
    st.markdown(c.models['MLOps_audience'])
    st.subheader("Why is it relevant?")
    st.markdown(
        c.models['MLOps_relevance'])
    st.link_button(
        "Go to Code",
        c.models['MLOps_code']
    )

