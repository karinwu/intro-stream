import streamlit as st

st.set_page_config(
    page_title="Self Introduction",
    page_icon="🏠",
    layout="wide"
)

tabs = st.tabs(
    [
        "🏠 Introduction",
        "❤️ Passion",
        "🎉 Fun Facts",
        "🔨 I made this",
    ]
)


with tabs[0]:
    st.header("About Me")
    st.subheader("Name")
    st.write("Karin Wu")
    st.subheader("Education")
    st.write("MSc in Data Science, Georgia Tech")

with tabs[1]:
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

with tabs[2]:
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


with tabs[3]:
    st.header("Things I've Made")
    st.subheader("🍰 Cake")
    st.image("cake_photo1.jpg", caption="Chocolate Cake", width=200)
    st.image("cake_photo2.jpg", caption="Fruit Tart", width=200)

    st.subheader("🧠 RNN")
    st.write("A Recurrent Neural Network project for text generation.")
    st.link_button("Go to Code", "https://github.com/karinrga")

    st.subheader("🤖 LLM")
    st.write("Built a Large Language Model demo for fun and learning.")
    st.link_button("Go to Code", "https://github.com/karinrga")

    st.subheader("📊 MLflow")
    st.write("Experiment tracking with MLflow for my ML projects.")
    st.link_button("Go to Code", "https://github.com/karinrga")
