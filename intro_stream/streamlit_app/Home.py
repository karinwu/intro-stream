import streamlit as st
import constants as c


st.set_page_config(
    page_title="About Me",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


if 'current_skills' not in st.session_state:
    st.session_state.current_skills = 'skills'

margin_r, body, margin_l = st.columns([0.4, 3, 0.4])


with body:
    c.menu()

    with st.sidebar:
        st.success("Select a page above.")

    st.header("About Me", divider='rainbow')

    col1, col2, col3 = st.columns([2, 0.2, 1])

    with col1:
        st.write(c.info['brief'])
        st.markdown(f"###### 😄 Name: {c.info['name']}")
        st.markdown(f"###### 📚 Education: {c.info['education']}")
        st.markdown(f"###### 🌏 Background: {c.info['background']}")
        st.markdown(f"###### 👀 Linkedin: {c.linkedin_link}")
        st.markdown(f"###### 👉 Github: {c.github_link}")

    st.markdown("<br>", unsafe_allow_html=True)


    show_real_skills = st.toggle("Show Real Skills", value=False)


    if show_real_skills:
        st.subheader("My :blue[REAL skills] ⚒️", divider='rainbow')
        current_skills = 'real_skills'
    else:
        st.subheader("My :blue[skills] ⚒️", divider='rainbow')
        current_skills = 'skills'

    def skill_tab(skills):
        rows, cols= len(skills)//c.skill_col_size, c.skill_col_size
        skills_iter = iter(skills)
        if len(skills) % c.skill_col_size != 0:
            rows += 1
        for x in range(rows):
            columns = st.columns(c.skill_col_size)
            for index_ in range(c.skill_col_size):
                try:
                    columns[index_].button(next(skills_iter))
                except StopIteration:
                    break

    with st.spinner(text="Loading section..."):
        if current_skills == 'skills':
            skill_tab(c.info['skills'])
        else:
            skill_tab(c.info['real_skill'])

with st.sidebar:
    st.success("Select a page above.")

    if show_real_skills:
        st.header("My REAL skills")
        for skill in c.info['real_skill']:
            st.write(f"- {skill}")
    else:
        st.header("My skills")
        for skill in c.info['skills']:
            st.write(f"- {skill}")
