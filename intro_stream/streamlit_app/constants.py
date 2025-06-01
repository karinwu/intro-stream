import streamlit as st

skill_col_size = 5


def menu():
    bar0, bar1, bar2, bar3, bar4 = st.columns([0.1, 1, 1, 1, 1])
    bar1.page_link("Home.py", label="Home", icon="🏠")
    bar2.page_link("pages/1_Fun_Facts.py", label="Fun Facts", icon="🎉")
    bar3.page_link("pages/2_Passion.py", label="Passion", icon="❤️")
    bar4.page_link("pages/3_I_Made_This.py", label="I Made This", icon="🔨")
    st.write("")


linkedin_logo = '''                                                                                                                        
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                              
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                    
'''


info = {'brief':
        """
          Full stack data scientist.

          Passionate about cakes, risk model, catastrophe model, renewable energy and climate tech.
        """,
        'name': 'Karin Wu',
        'background': 'Born in Shanghai, lived in 6 different counties',
        'education': 'MSc in Data Science, Georgia Tech',
        'skills': ['Python', 'R', 'SQL', 'PyTorch', 'Docker', 'Kubernetes',
                   'DBT', 'GCP', 'AWS', 'Git', 'LangGraph', 'fastAPI',
                   'RAG', 'LLM', 'Pipelines'],
        'real_skill': ['Google everything',
                       'Ask ChatGPT',
                       'Debugging',
                       'Procrastination',
                       'Overthinking',
                       'Eating snacks while coding'],
        }

linkedin_link = "https://www.linkedin.com/in/karinwu8/"
github_link = "https://github.com/karinwu"

facts = {
    'family': "I have a wonderful family of three.",
    'countries': "I've lived in 6 countries! ",
}

passions = {
    'cakes': "I love baking and decorating cakes.",
    'swimming': "Swimming keeps me active and refreshed.",
    'renewable_energy': "I believe in eletrify everything to decarbonize the grid and fight climate change."
}
