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

# Add a deploy button (for demonstration purposes)
st.button("Deploy")

elif page == "Model Analysis":
    st.write("This page will contain model analysis")
    # Placeholder for model analysis content
    # You can add charts, metrics, etc. here
    st.write("Model analysis content will be added here.")

    # Example placeholder data for analysis
    data = pd.DataFrame({
        'Category': ['Technology', 'Health', 'Business', 'Entertainment', 'Sports'],
        'Count': [50, 20, 30, 40, 25]
    })

    # Chart example for Model Analysis page
    chart = alt.Chart(data).mark_bar().encode(
        x='Category',
        y='Count'
    ).properties(
        title='News Articles by Category'
    )
    st.altair_chart(chart, use_container_width=True)

elif page == "Upload Data":
    st.header("Upload your CSV data file")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file is not None:
        # Read the CSV file
        data = pd.read_csv("test.csv")

        # Display the dataframe
        st.write(data)
