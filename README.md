# Simple Data Science Streamlit App
This is a simple data science app that takes a data set about Data Scientists
and runs a pandas profiling package on them. This is for demonstration purposes
to show how easy it is to create and share an app to Streamlit Sharing.

## Directories
**data/:** holds the data used in the App

**modules/:** holds the python files for the 3 "pages" of my Streamlit app
- **home_page.py:** has the code to generate the landing page for the App
- **pandas_page.py:** has the code to use the pandas profiling Streamlit component
  to generate an in depth profile of each feature in our data
- **graphs_page.py:** has the code to auto generate some bar graphs for each of
    the features in our dataset
