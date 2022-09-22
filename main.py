import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

from DataViz.plot_account_activity import *

st.set_page_config(layout="wide")

data = pd.read_csv("../micro_world.csv")
ph_data =  data[data['economy']=='Philippines']

def load_data():
    # Load the data
    data = pd.read_csv(
        "data/micro_world.csv"
    )
    return data

def overview():
    pass

def look_account_ownership():
    col1, col2 = st.columns([5,7])

    with col1:
        st.pyplot(has_an_account(ph_data))


    with col2:
        option = st.selectbox(
             'What would you like to see?',
             ('Account Activity', 'Mobile Activity', 'Others'))
        st.write('You selected:', option)
        if (option) == 'Mobile Activity':
            st.pyplot(plot_mobile_activity(ph_data))
        elif (option) == 'Account Activity':
            st.pyplot(plot_account_activity(ph_data))
        else :
            st.write('PLOT COMING SOON! ^_^')

    
def digital_overview():
    pass

def clusters():
    pass

def recommendations():
    pass

def the_team():
    pass


list_of_pages = [
    "Overview",
    "Look Account Ownership",
    "Digital Overview",
    "Clustering",
    "Recommendations",
    "The Team"
]

## streamlit layout 

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Overview":
    overview()

elif selection == "Look Account Ownership":
    look_account_ownership()

elif selection == "Digital Overview":
    digital_overview()

elif selection == "Clustering":
    clusters()

elif selection == "Recommendations":
    recommendations()

elif selection == "The Team":
    the_team()
