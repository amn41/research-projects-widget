import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

st.beta_set_page_config(page_title="Research projects widget",initial_sidebar_state='expanded')
st.title('Resarch projects')

explanation = """
This widget is a simple way to show the potential impact of research projects.
You can use the sidebar to adjust your estimates of the likely impact of different
projects on the capabilities of assistants built with Rasa (i.e. what the most advanced
teams can build) and Rasa's ease of use (i.e. how many teams are able to build with Rasa).
You can also estimate the difficulty/ uncertainty of each project. Higher-risk projects
are shown in a lighter colour on the plot.

The hope is that in aggregate we can get a feel for how we are investing our time.
"""

st.text(explanation)

projects = {
    "end to end": {'effort': 10, 'capabilities':80, 'difficulty': 80},
    "knowledge bases": {'effort': 20, 'capabilities':80, 'difficulty': 70},
    "paraphrasing": {'effort': 70, 'capabilities':30, 'difficulty': 50}
    }

project_name = st.sidebar.selectbox(
    "Choose Project",
    list(projects.keys())
)

effort = st.sidebar.slider('effort', 0, 100, projects[project_name]['effort'])
capabilities = st.sidebar.slider('capabilities', 0, 100, projects[project_name]['capabilities'])
difficulty = st.sidebar.slider('difficulty', 0, 100, projects[project_name]['difficulty'])

## update dict with new slider vals, if edited
projects[project_name]['effort'] = effort
projects[project_name]['capabilities'] = capabilities
projects[project_name]['difficulty'] = difficulty


## set up plot basics
cmap = get_cmap('Blues')
fig, ax = plt.subplots()

for project_name, data in projects.items():
    color = cmap((100-data['difficulty'])/100)
    ax.arrow(0, 0.0, data['capabilities'], data['effort'], head_width=0.5, head_length=0.7, ec=color, linewidth=8.)
    ax.text(data['capabilities']+4, data['effort'] ,project_name)

# clean up plot
ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("Capabilities of assistants built with Rasa")
ax.set_ylabel("Ease of use of Rasa")

st.pyplot(fig)
