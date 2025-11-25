import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("cat_dog_model.pkl")

st.set_page_config(page_title="Cat-Dog Predictor", page_icon="🐾")

st.title("🐱🐶 Cat–Dog Prediction App")
st.write("Provide the characteristics below and click **Predict**.")

# User inputs
height = st.number_input("Height", min_value=0.0)
weight = st.number_input("Weight", min_value=0.0)

ear_shape = st.selectbox("Ear Shape", ["pointy", "floppy"])
tail = st.selectbox("Tail Type", ["long", "short"])

# When button clicked
if st.button("Predict"):
    # Create DataFrame for prediction
    input_data = pd.DataFrame({
        "Height": [height],
        "Weight": [weight],
        "Ear Shape": [ear_shape],
        "Tail": [tail]
    })

    # Predict
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == "Cat":
        st.success("🐱 Prediction: **Cat**")
    else:
        st.success("🐶 Prediction: **Dog**")
