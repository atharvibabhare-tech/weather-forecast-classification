import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('weather_model.pkl', 'rb'))

# Weather labels
weather_labels = {
    0: 'Cloudy',
    1: 'Rainy',
    2: 'Sunny'
}

st.set_page_config(
    page_title="Weather Prediction ML",
    page_icon="🌦️",
    layout="centered"
)

st.title("🌦️ Weather Prediction System")

st.write(
    "Predict weather conditions using atmospheric parameters."
)

# User Inputs
temperature = st.number_input(
    "Temperature",
    min_value=-50.0,
    max_value=60.0,
    value=30.0
)

humidity = st.number_input(
    "Humidity",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

wind_speed = st.number_input(
    "Wind Speed",
    min_value=0.0,
    max_value=200.0,
    value=10.0
)

pressure = st.number_input(
    "Pressure",
    min_value=800.0,
    max_value=1200.0,
    value=1005.0
)

# Prediction Button
if st.button("Predict Weather"):

    sample = np.array([
        [temperature, humidity, wind_speed, pressure]
    ])

    prediction = model.predict(sample)[0]

    weather = weather_labels.get(
        prediction,
        "Unknown"
    )

    st.success(f"Predicted Weather: {weather}")
