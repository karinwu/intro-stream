import streamlit as st

st.set_page_config(
    page_title="3. I Made This",
    page_icon="🔨",
    layout="wide"
)

st.header("Cakes I've Made")

st.subheader("🍰 Cake")
col1, col2 = st.columns(2)

with col1:
    st.image(
        "images/cake_1.jpeg",
        caption="Strawberry Cake",
        use_container_width=True
    )
with col2:
    st.image(
        "images/cake_2.jpeg",
        caption="Thomas Cake",
        use_container_width=True
    )

# List of images and captions
# images = [
#     ("images/cake_1.jpeg", "Strawberry Cake"),
#     ("images/cake_2.jpeg", "Thomas Cake"),
#     ("images/cake_3.jpeg", "Lemon Cake"),
#     ("images/cake_4.jpeg", "Chocolate Cake"),
#     ("images/cake_5.jpeg", "Vanilla Cake"),
#     ("images/cake_6.jpeg", "Birthday Cake"),
#     ("images/cake_7.jpeg", "Fruit Tart"),
#     ("images/cake_8.jpeg", "Berry Cake"),
#     ("images/cake_9.jpeg", "Cheesecake"),
#     ("images/cake_10.jpeg", "Rainbow Cake"),
#     ("images/cake_11.jpeg", "Cupcake"),
#     ("images/cake_12.jpeg", "Wedding Cake"),
#     ("images/cake_13.jpeg", "Pineapple Cake"),
#     ("images/cake_14.jpeg", "Red Velvet"),
#     ("images/cake_15.jpeg", "Carrot Cake"),
#     ("images/cake_16.jpeg", "Mini Cake"),
# ]

# # Display in 4 by 4 grid
# for i in range(0, len(images), 4):
#     cols = st.columns(4)
#     for j in range(4):
#         if i + j < len(images):
#             with cols[j]:
#                 img_path, caption = images[i + j]
#                 st.image(img_path, caption=caption, use_column_width=True)

st.header("Models I've Made")

st.subheader("🧠 RNN")
st.write("A Recurrent Neural Network project for text generation.")
st.link_button("Go to Code", "https://github.com/karinwu")

st.subheader("🤖 LLM")
st.write("Built a Large Language Model demo for fun and learning.")
st.link_button("Go to Code", "https://github.com/karinwu")

st.subheader("📊 MLOps")
st.write("Experiment tracking with MLflow for my ML projects.")
st.link_button("Go to Code", "https://github.com/karinwu")
