from gettext import install
# from turtle import width
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
import lorem 


from DataViz.plot_account_activity import *
from DataViz.digital_access import *
from DataViz.reasons import *
from DataViz.received_payment import received_payment
from add_background import add_bg_from_local

# # settings for all of the pages in the app
st.set_page_config(layout="wide")

# add_bg_from_local('images/test_img1_soft.png')

# # set css settings
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# setting plot color themes
sns.set_theme(style="white", palette=sns.color_palette("Set2"))

# load the data 
data = pd.read_csv("data/micro_world.csv")
ph_data =  data[data['economy']=='Philippines']

def load_data():
    # Load the data
    data = pd.read_csv(
        "data/micro_world.csv"
    )
    return data

def overview():
    st.title('Bridging the gap in financial inclusion in the Philippines through digital finance')
    col1, col2, col3 = st.columns([1,10,1])
    with col1:
        st.write("")

    with col2:
        st.image('images/diskartech.png', width = 800, caption = 'this is a sample caption') # width is in pixels?

    with col3:
        st.write("")
    
    st.write('''
        A [study](https://bsc.cid.harvard.edu/files/bsc/files/2021-05-cid-wp-398-development-_delivers.pdf) 
    from harvard shows the higher the countriesâ€™ social progress index, the higher its level of national development. 
    Social progress index is the average of basic human needs like:
     - Basic human needs (i.e. nutrition)
     - Foundations of well being (i.e. access to basic knowledge)
     - Opportunity (i.e. personal rights)
    This tell us that no country with low levels of national development has high levels of human well being.
    One way of national development is financial inclusion since it is a state in which everyone (especially vulnerable sectors)
    has effective access to a wide range of financial services that could boost the economy.
    ''')
    st.write("")
    st.write(''' 
    Using the [Global Financial Inclusion (Global Findex) Database 2017](https://microdata.worldbank.org/index.php/catalog/3324/data-dictionary/F2?file_name=micro_world),
    a comprehensive data set on how adults save, borrow, make payments, and manage risk. 
    ''')

    with st.container():
        col1, col2, col3 = st.columns((1,9,1))
        with col1:
            pass
        with col2:
            st.write("")
            st.write("")
            st.pyplot(received_payment(ph_data))

        with col3:
            pass
    
    st.write(''' 
    An exploration into this data revealed that the **Philippines is still heavily reliant in cash as a method of payment**.
    ''')
    st.write("")
    


def look_account_ownership():
    st.header('What is the status of account ownership among Filipinos?')

    col1, col2, col3 = st.columns((2,8,2))
    with col1:
        pass
    with col2:
        st.write("")
        st.write("")
        st.pyplot(has_an_account(ph_data))

    with col3:
        pass
   
    st.write(''' 
    In 2017, the majority of Filipinos were found to not own a financial account. For those with an account, majority have an account in financial institutions only.
    Interestingly, those with mobile money only were found to be the least**.
    ''')
    st.write("")

    st.header('According to the survey, why are the unbanked Filipinos still unbanked?')

    col1, col2, col3 = st.columns((2,8,2))
    with col1:
        pass

    with col2:
        st.write("")
        st.write("")
        st.pyplot(reasons_no_account(ph_data))

    with col3:
        pass

    st.write(''' 
    The main reason is - Filipinos do not have enough money to use financial services. This is followed by Filipinos thinking that financial services are too expensive and that they do not have the necessary documentation to open such accounts.
    
    Insights:

    1. Most Filipinos are unbankable since they do not have enough money to open an account.
    2. The requirements in opening an account might be too rigid for the Filipino population.
    ''')
    st.write("")

    
def digital_overview():

    st.header('Digital Finance will bridge the gap in account ownership')

    st.write('''
    
    ''')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('3 in 10 Filipinos has an account')
        st.pyplot(has_an_account(ph_data))

    with col2:
        st.subheader('7 in 10 Filipinos owns a mobile phone')
        st.pyplot(has_mobile_phone(ph_data))

    
    st.write('''Despite having a large number of individuals owning a mobile phone and the availability of digital financial services, only 1 in 10 Filipinos 
    actually use their phones for financial transactions. 
    This presents an opportunity to introduce digital finance as a tool to make other financial services available to the different people 
    - especially to the unbanked who have mobile phones. ''')

    with st.container():
        col1, col2, col3 = st.columns((2,8,2))
        with col1:
            pass
        with col2:
            st.write("")
            st.write("")
            st.subheader('Only 1 in 10 Filipinos uses mobile financial services')
            st.pyplot(digital_access(ph_data))

        with col3:
            pass
    
    st.write('''This low utilization of mobile financial services becomes more apparent when we compare it with utilization across the Southeast Asia region.
    The Philippines falls in the bottom four in terms of digital financial access in the region. 
    ''')

    with st.container():
        col1, col2, col3 = st.columns((2,8,2))
        with col1:
            pass
        with col2:
            st.write("")
            st.write("")
            st.pyplot(digital_access_sea(data))

        with col3:
            pass
   
   


def clusters():
    st.title('Financial Inclusion Segments')
    st.subheader('We identified 5 segments of financial inclusion to understand the different attitudes and needs of each group.')

    with st.container():
        col1, col2 = st.columns([8,4])

        with col1:
            st.image('images/clusters.png')
            
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
            
    st.markdown('***')
    st.subheader('Insigths')        
    with st.container():
        col1, col2 = st.columns([1,2])

        with col1:
            st.write(
                '''
                - We can see that all excluded segments have similar pain points with having not enough money to use FI as the greatest barrier, 
                followed by financial services being too expensive. For these groups, cost is the main driver that discourages them from availing financial services.
                - Other notable barriers are having no necessary documentation and financial institutions being too far away.
                '''
            )
        with col2:
            st.image('images/radar_chart.png')

def recommendations():
    st.title('Recommendations')
    # st.subheader('placeholder')

    st.markdown('***')
    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/local_initiatives.png')
        with col2:
            title = '<p style="font-size: 30px;"><b>Expand local initiatives</b> that uses e-wallets as payment solutions.</p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - In 2018, the city of Valenzuela partnered with Maya to transform one of their public markets into a â€śDigiPalengkeâ€ť.
                - In 2020, Makati City, Muntinlupa City used GCash for digital 'ayuda' distribution. 
                '''
            )
    st.markdown('***')
    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/ads.png')
        with col2:
            title = '<p style="font-size: 30px;">Create <b> targeted and more inclusive advertising.</b></p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - Partner with local influencers to promote currently available financial products and services.
                '''
            )
    st.markdown('***')
    with st.container():
        col1, col2 = st.columns([1,1])

        with col1:
            st.image('images/literacy.png')
        with col2:
            title = '<p style="font-size: 30px;"><b>Financial Literacy</b> programs for school-age children.</p>'
            st.markdown(title, unsafe_allow_html=True)
            st.write(
                '''
                - Financial institutions and experts can work with schools, non-governmental organisations (NGOs) and communities to deliver financial education programmes to school-age children.
                - An example of this is the Peso Smart - Manulifeâ€™s financial literacy program
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

            name = '<p style="font-size: 30px;"><b>Sofia Adriana L. Calvo</b></p>'
            st.markdown(name, unsafe_allow_html= True)
            st.write("email: sofiaacalvo@gmail.com")
            st.write("linkedin: https://www.linkedin.com/in/sofiaadrianacalvo")
            st.write("github: https://github.com/sofadrianacalvo")
        
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

            name = '<p style="font-size: 30px;"><b>Rex G. Fuentes</b></p>'
            st.markdown(name, unsafe_allow_html= True)
            st.write("email: rexfuentes@gmail.com")
            st.write("linkedin: https://www.linkedin.com/in/rex-f-b425ab249/")
            st.write("github: https://github.com/code18524")



list_of_pages = [
    "Overview",
    "Account Ownership",
    "Digital Overview",
    "Financial Inclusion Segments",
    "Recommendations",
    "The Team"
]

## streamlit layout 

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Overview":
    overview()

elif selection == "Account Ownership":
    look_account_ownership()

elif selection == "Digital Overview":
    digital_overview()


elif selection == "Financial Inclusion Segments":
    clusters()

elif selection == "Recommendations":
    recommendations()

elif selection == "The Team":
    the_team()
