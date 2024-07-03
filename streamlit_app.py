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
    st.write(f"Entered Text: {text}

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Streamlit app
st.title("ML Model Prediction and Confusion Matrix")

# Sidebar for model selection
model_option = st.sidebar.selectbox('Select Model', ['Logistic Regression', 'Support Vector Classifier'])

# Sidebar for model parameters
test_size = st.sidebar.slider('Test Size', 0.1, 0.5, 0.25)
random_state = st.sidebar.slider('Random State', 0, 100, 42)
kernel = st.sidebar.selectbox('SVM Kernel', ['linear', 'rbf']) if model_option == 'Support Vector Classifier' else None

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the selected model
if model_option == 'Logistic Regression':
    model = LogisticRegression(max_iter=200)
elif model_option == 'Support Vector Classifier':
    model = SVC(kernel=kernel)

model.fit(X_train, y_train)

# Predict the test set results
y_pred = model.predict(X_test)

# Generate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
st.subheader(f'{model_option} Confusion Matrix')
fig, ax = plt.subplots()
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap='Blues', ax=ax)
st.pyplot(fig)

# Display accuracy
accuracy = (y_pred == y_test).mean()
st.write(f'Accuracy: {accuracy:.2f}')

# Display the confusion matrix as a heatmap
st.subheader('Confusion Matrix Heatmap')
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
st.pyplot(fig)

# Calculate recall for each class
recall_values = recall_score(y_test, y_pred, average=None)
sports_recall = recall_values[0]  # Assuming 'sports' is the first class
education_recall = recall_values[1]  # Assuming 'education' is the second class

# Creating a DataFrame for recall comparison
df = pd.DataFrame({
    'Models': ['Logistic Regression', 'Support Vector'],
    'Sports': [0.81, 0.96],  # Replace with actual recall values if available
    'Education': [0.97, 0.94]  # Replace with actual recall values if available
})

# Plotting recall comparison
st.subheader('Recall Comparison')
fig, ax = plt.subplots()
df.plot(x="Models", y=["Sports", "Education"], kind="bar", ax=ax)
plt.xlabel('Models')
plt.ylabel('Recall')
plt.xticks(rotation=20)
st.pyplot(fig)

# Add a deploy button (for demonstration purposes)
st.button("Deploy")


  
  
