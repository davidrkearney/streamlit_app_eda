import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def run_pandas(train_set):
    st.header(":scales: Pandas Profiling Report")
    st.write()
    pr = ProfileReport(train_set, explorative=True)
    st_profile_report(pr)
    return
