import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import numpy as np

def run_pandas(train_set):
    progress_bar = st.progress(0)
    status_text = st.empty()
    progress_bar.progress(0.1)

    st.header(":scales: Pandas Profiling Report")
    st.write()
    pr = ProfileReport(train_set, explorative=True)
    st_profile_report(pr)

    status_text.text('Done!')
    st.balloons()
    progress_bar.progress(0.9)

    return
