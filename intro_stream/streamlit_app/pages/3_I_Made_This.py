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
    st.write(
        "A Temporal Graph Neural Network (GNN) model for short-term forecasting."
    )
    st.subheader("Who is it for?")
    # st.write("Who is it for?")
    st.write(
        "For researchers and developers interested in time-series forecasting "
        "using graph neural networks."
    )
    st.subheader("Why is it relevant?")

    st.write(
        "Temporal GNNs can capture complex temporal dependencies in data, "
        "making them suitable for tasks like forecasting pandemic outcome in "
        "health insurance industry."
    )
    st.link_button(
        "Go to Code",
        "https://github.com/karinwu/short-term-forecast/blob/main/short_term_forecast/model")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<h3 style="color:green;">🤖 LLM</h3>',
        unsafe_allow_html=True
    )

    st.subheader("What is it?")
    st.write(
        "A Large Language Model (LLM) demo that provides insights "
        "into permit data."
    )
    st.subheader("Who is it for?")
    st.write(
        "For developers and data scientists interested in "
        "building applications "
        "that leverage LLMs for data insights and analysis."
    )
    st.subheader("Why is it relevant?")
    st.write(
        "Understand how RAG provides a robust knowledge base for LLMs, "
        "helps second line of defense to validate the model risks,"
        "identify potential biases, and ensure ethical use of AI."
    )

    st.link_button(
        "Go to Code",
        "https://github.com/karinwu/llm-permit-insights-pipeline"
    )

    st.markdown("<br>", unsafe_allow_html=True)    
    st.markdown(
        '<h3 style="color:green;">📊 MLOps</h3>',
        unsafe_allow_html=True
    )    
    st.subheader("What is it?")
    st.write(
        "A Machine Learning Operations (MLOps) pipeline "
        "that automates the model lifecycle."
    )
    st.subheader("Who is it for?")
    st.write(
        "For data scientists and machine learning engineers looking to "
        "implement MLOps practices in their projects."
    )
    st.subheader("Why is it relevant?")
    st.write(
        "MLOps practices help streamline the model lifecycle, "
        "tracks every artifacts of the model, particularly useful for "
        "the second line of defnese in evaluating model risks and "
        "validate model performance."
    )
    st.link_button("Go to Code", "https://github.com/karinwu/mlops")
