import streamlit as st
import pandas as pd

#import python pages
from modules.home_page import run_home
from modules.pandas_page import run_pandas
from modules.graphs_page import run_graphs

#Set app name and emoji displayed in browser tab
st.set_page_config(page_title="Fiscal Data", page_icon="bar_chart")

#title of my app and brief description
st.title("Fiscal Data")
st.subheader("Let's take a look at some Fiscal Data! :face_with_monocle:")

#set up the side bar for page options
page = st.sidebar.radio("Pick a Page:", ["Home", "Pandas Profile", "Basic Graphs"])

#load data
#url = 'https://raw.githubusercontent.com/davidrkearney/Kearney_Data_Science/master/_notebooks/df_panel_fix.csv'
url = 'https://raw.githubusercontent.com/davidrkearney/colab-notebooks/main/datasets/depression_data.csv'
train_set = pd.read_csv(url, error_bad_lines=False)

if page == "Home":
    run_home(train_set)

elif page == "Pandas Profile":
    run_pandas(train_set)

else:
    run_graphs(train_set)
