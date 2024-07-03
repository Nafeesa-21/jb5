import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#-----------sidebar
page = st.sidebar.selectbox('page navigator', ["predictor", "model analyis"])
