from gettext import install
from turtle import width
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
import lorem 
import base64


from DataViz.plot_account_activity import *
from add_background import add_bg_from_local

# # settings for all of the pages in the app
st.set_page_config(layout="wide")

add_bg_from_local('images/test_img1_soft.png')

# # set css settings
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# load the data 
data = pd.read_csv("../micro_world.csv")
ph_data =  data[data['economy']=='Philippines']

def load_data():
    # Load the data
    data = pd.read_csv(
        "data/micro_world.csv"
    )
    return data

def overview():
    st.title('Digital Financial Access in the Philippines: An Opportunity for Financial Inclusion')
    st.subheader('this is a subheader')
    st.image('images/test_img1.png', width = 800) # width is in pixels?
    st.caption('this is a caption')
    st.write(lorem.paragraph())

def look_account_ownership():
    st.header('Account Ownership in 2017')

    st.pyplot(has_an_account(ph_data))


    with st.container():
        col1, col2 = st.columns([5,7])
        
        with col1:
           st.write(lorem.paragraph())

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
