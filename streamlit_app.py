import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#-----------sidebar
page = st.sidebar.selectbox('page navigator', ["predictor", "model analyis"])

if page == "predictor":
  #-----------inputs
  st.markdown("Analysing news articles")
  upload_columns = st.columns([2,1])
  # file upload
file_upload = upload_columns[0].expander(label="prediction with ml flows")


  
  
