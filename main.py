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
    st.title('Clustering')
    st.subheader('this is subheader')

    with st.container():
        col1, col2 = st.columns([3,1.5])

        with col1:
            st.image('images/clusters.png', width = 800)
            
        with col2:
            option = st.selectbox(
                '',
                ('Cash Savers', 'Modern Savers', 'Supported', 'Underserved & Vulnerable', 'Money Segregators')
            )
            if option == 'Cash Savers':
                st.image('images/cashsavers.png')
                st.write(
                    '''
                    This group is the largest among the clusters. 
                    Their employment and income gave them the propensity to save money. 
                    However, they do not own any type of financial account.
                    ''')
            elif option == 'Modern Savers':
                st.image('images/modernsavers.png')
                st.write(
                    '''
                    This group belongs to the richest 20% 
                    so they have the means to save and tie it up to a financial account.
                    ''')
            elif option == 'Supported':
                st.image('images/supported.png')
                st.write(
                    '''
                    This group has no income and savings 
                    ''')
            elif option == 'Underserved & Vulnerable':
                st.image('images/vulnerable.png')
                st.write(
                    '''
                    These people are employed but have no savings because they are living paycheck to paycheck.
                    ''')

            elif option == 'Money Segregators':
                st.image('images/segregators.png')
                st.write('''
                These are people who have no savings but have accounts they use for other purposes like 
                receiving/giving payments, receiving/giving remittances and etc.
                ''')
            
    st.subheader('Insigths')        
    with st.container():
        col1, col2 = st.columns([1,2])

        with col1:
            st.write(
                '''
                - something
                - somthing
                '''
            )
        with col2:
            st.image('images/radar_chart.png')

def recommendations():
    st.title('Recommendations')
    st.subheader('placeholder')

    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/local_initiatives.png')
        with col2:
            title = '<p style="font-size: 30px;"><b>Expand local initiatives</b> that uses e-wallets as payment solutions.</p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - something
                - something
                '''
            )
    
    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/ads.png')
        with col2:
            title = '<p style="font-size: 30px;">Create <b> targeted and more inclusive advertising.</b></p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - something
                - something
                '''
            )
    
    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/literacy.png')
        with col2:
            title = '<p style="font-size: 30px;"><b>Financial Literacy</b> programs for school-age children.</p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - something
                - something
                '''
            )


def the_team():
    st.title('The Team')
    with st.container():
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            name = '<p style="font-size: 30px;"><b>Karen Chrisele M. Bioy</b></p>'            
            st.markdown(name, unsafe_allow_html=True)
            st.write("email: kcbioy@gmail.com")
            st.write("linkedin: https://www.linkedin.com/in/kcbioy/")
            st.write("github: https://github.com/kcbioy")
            st.write("")
            st.write("")
            st.write("")

            st.markdown("**Name**")
            st.write("something")

        
        with col2:
            name = '<p style="font-size: 30px;"><b>Chiara Gabrelle S. Perez</b></p>'
            st.markdown(name, unsafe_allow_html= True)
            st.write("email: chiaraperez2000@gmail.com")
            st.write("linkedin: https://www.linkedin.com/in/chiara-perez/")
            st.write("github: https://github.com/chiaperez")
            st.write("")
            st.write("")
            st.write("")

            name = '<p style="font-size: 30px;"><b>Enrico Jose M. Asuncion</b></p>'
            st.markdown(name, unsafe_allow_html= True)
            st.write("email: ejmasuncion@yahoo.com")
            st.write("linkedin: https://www.linkedin.com/in/ejmasuncion/")
            st.write("github: https://github.com/ejmasuncion")

        
        with col3:
            name = '<p style="font-size: 30px;"><b>Ma. Karla Coleen G. Concepcion</b></p>'
            st.markdown(name, unsafe_allow_html= True)
            st.write("email: karlacoleenconcepcion@gmail.com")
            st.write("linkedin: https://www.linkedin.com/in/karlacoleenconcepcion")
            st.write("github: https://github.com/karlacoleen")
            st.write("")
            st.write("")
            st.write("")

            st.markdown("**Name**")
            st.write("something")



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
