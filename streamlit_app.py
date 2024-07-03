import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#-----------sidebar
page = st.sidebar.selectbox('page navigator', ["predictor", "model analyis"])

# Set the title of the app
st.title("News Classifier")

# Add a description
st.write("Analyzing news articles")

# Text input for news articles
text = st.text_area("Enter Text", "")

# Button to classify the news article
if st.button("Classify"):
    # This is where the ML model prediction would happen
    # For now, we'll just display the entered text
    # You would replace this with your model's prediction logic
    st.write("Prediction with ML Models")
    st.write(f"Entered Text: {text}")

# Comparing Recall for the sports and education to support the final decision on
# best performing model
df = pd.DataFrame({
    'Models': ['Logistic regression', 'Support vector'],
    'sports': [0.81, 0.96],
    'education': [0.97, 0.94]
})

# plotting graph
df.plot(x="Models", y=["sports", "education"], kind="bar")
plt.xlabel('Models')
plt.ylabel('Recall')
plt.xticks(rotation=20)
# Add a deploy button (for demonstration purposes)
st.button("Deploy")


  
  
