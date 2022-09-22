import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


def load_data():
    # Load the data
    data = pd.read_csv(
        "data/micro_world.csv"
    )
    return data

def overview():
    pass

def look_account_ownership():
    pass

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
    "Clustering",,
    "Recommendations",
    "The Team"
]