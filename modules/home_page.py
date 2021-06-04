import streamlit as st
import pandas as pd

def run_home(data):
    st.header(":house_with_garden: Homepage")
    st.write("""Lets look at the data.""")
    display_data = st.empty()

    slider_value = st.slider("pick a number", 0, len(data), (0,500), 500)
    st.write(slider_value,slider_value[0],slider_value[1])

    display_data.dataframe(data.loc[slider_value[0]:slider_value[1]])
    #display_data.dataframe(data)

    st.subheader("Features of the data")
    
    #url = st.text_input("data url", 1)



    st.write("""

* **Year:** Year in the data set
    * Time window
* **Year:** Year in the data set
    * Time window
* **target:** If your going to run some machine learning methods, this is the intended column for predictions
    * Consists of 2 categories: 


    """)
    return
