import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_graphs(train_set):
    st.header(":chart_with_upwards_trend: Basic Graphs")
    st.write("""Lets create some basic graphs with the data as is. These won't
look perfect as they are auto-generated but lets get some visuals of what we are working with:""")
    #make a multiselect for the features to display
    features = list(train_set.columns)
    choice = st.multiselect("Pick one or more features to look at", features[2:])

    if len(choice) > 0:
        for val in choice:
            column = train_set[val].dropna().squeeze() # makes a series out of the column
            unique = column.unique()
            #st.write(type(column), unique)

            fig = plt.figure()
            ax= fig.add_subplot(111)

            plt.hist(column)
            plt.title(val)
            plt.ylabel("Counts")

            st.pyplot(fig)
