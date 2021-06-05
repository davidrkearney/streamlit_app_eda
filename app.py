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
page = st.sidebar.radio("Pick a Page:", ["Home", "Pandas Profile", "Basic Graphs", "Audio Page"])

import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.title("Plotly examples")

st.header("Chart with two lines")

trace0 = go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])
trace1 = go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9])
data = [trace0, trace1]
st.write(data)





#load data
#url = 'https://raw.githubusercontent.com/davidrkearney/Kearney_Data_Science/master/_notebooks/df_panel_fix.csv'
#url = 'https://raw.githubusercontent.com/davidrkearney/colab-notebooks/main/datasets/depression_data.csv'
#url='https://raw.githubusercontent.com/davidrkearney/colab-notebooks/main/datasets/diabetes.csv'
url='https://stocks-snp-500.herokuapp.com/stocks/turnover_tables.csv?_size=max'

train_set = pd.read_csv(url, error_bad_lines=False)

if page == "Home":
    run_home(train_set)

elif page == "Pandas Profile":
    run_pandas(train_set)

elif page == "Audio Page":
    run_audio()

else:
    run_graphs(train_set)
