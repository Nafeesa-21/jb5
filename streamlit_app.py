import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#-----------sidebar
page = st.sidebar.selectbox('page navigator', ["predictor", "model analyis"])

if page == "predictor":
  #-----------inputs
  st.markdown("analysing news articles")
  columns = st.columns([2,1])
  
  # model input
  model_input = column[0].expander(label="prediction with ML models")
  
  
