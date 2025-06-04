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
        'background': 'Born in Shanghai',
        'education': 'MSc in Data Science, Georgia Tech',
        'skills': ['Python', 'R', 'SQL', 'PyTorch', 'Docker', 'Kubernetes',
                   'DBT', 'GCP', 'AWS', 'Git', 'LangGraph', 'Airflow',
                   'Snowflake', 'RAG', 'LLM' ]
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
    'cakes': "I love baking and decorating cakes and cookies.",
    'swimming': "Swimming keeps me active and refreshed.",
    'renewable_energy': "I believe in eletrify everything with clean energy"
    " to decarbonize the grid and fight climate change.",
    'project': "Contributed to the Elecficiation Impact Study for "
    "California Utility Commission (CPUC) to determine the distribution grid "
    "planning and requirements. ",
    "bess": "Created battery adoption models and battery behavioral simulation "
    "for Tesla Powerwall.",
}


models = {
    'GNN': "A Temporal Graph Neural Network (GNN) model for short-term"
    " forecasting.",
    'GNN_audience': "For researchers and developers interested in "
    "time-series forecasting using graph neural networks.",
    'GNN_relevance': "Temporal GNNs can capture complex temporal "
    "dependencies in data, making them suitable for tasks like "
    "forecasting pandemic outcome in health and life insurance.",
    'GNN_code': "https://github.com/karinwu/short-term-forecast/blob/"
    "main/short_term_forecast/model",

    'LLM': "A Large Language Model (LLM) demo that provides insights "
    "into permit data.",
    'LLM_audience': "For developers and data scientists interested in "
    "building applications "
    "that leverage LLMs for data insights and analysis.",
    'LLM_relevance': "Understand how RAG provides a robust knowledge base for "
    "LLMs, helps second line of defense to validate the model risks,"
    "identify potential biases, and ensure ethical use of AI.",
    'LLM_code': "https://github.com/karinwu/llm-permit-insights-pipeline",

    'MLOps': "A Machine Learning Operations (MLOps) pipeline that "
    "automates the end-to-end machine learning ",
    'MLOps_audience': "For data scientists and machine learning engineers "
    "looking to implement MLOps practices in their projects.",
    'MLOps_relevance':  "MLOps practices help streamline the model lifecycle, "
    "tracks every artifacts of the model, particularly useful for "
    "the second line of defnese in monitoring error metrics, parameters, "
    "evaluating model risks and "
    "validate model performance.",
    'MLOps_code': "https://github.com/karinrwu/mlops"
    }
