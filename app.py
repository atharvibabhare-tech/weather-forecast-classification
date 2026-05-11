import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('weather_model.pkl', 'rb'))

# Weather Labels
weather_labels = {
    0: "Cloudy ☁️",
    1: "Rainy 🌧️",
    2: "Sunny ☀️"
}

# Page Config
st.set_page_config(
    page_title="Weather Forecast Classification",
    page_icon="🌦️",
    layout="centered"
)

# Title
st.title("🌦️ Atmospheric Weather Classification System")

st.write(
    """
    Predict weather conditions using atmospheric parameters
    such as temperature, humidity, wind speed, and pressure.
    """
)

# City Input
city = st.text_input(
    "City Name",
    placeholder="Enter city name"
)

# User Inputs
temperature = st.number_input(
    "Temperature (°C)",
    min_value=-50.0,
    max_value=60.0,
    value=30.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

wind_speed = st.number_input(
    "Wind Speed (km/h)",
    min_value=0.0,
    max_value=200.0,
    value=10.0
)

pressure = st.number_input(
    "Pressure (hPa)",
    min_value=800.0,
    max_value=1200.0,
    value=1005.0
)

# Prediction Button
if st.button("Predict Weather"):

    # Input Data
    sample = np.array([
        [temperature, humidity, wind_speed, pressure]
    ])

    # Prediction
    prediction = model.predict(sample)[0]

    # Weather Output
    weather = weather_labels.get(prediction, "Unknown")

    # Display Results
    st.success(f"Predicted Weather Condition: {weather}")

    st.subheader("Weather Analysis")

    st.write(f"📍 City: {city if city else 'Not Provided'}")
    st.write(f"🌡️ Temperature: {temperature} °C")
    st.write(f"💧 Humidity: {humidity}%")
    st.write(f"🌬️ Wind Speed: {wind_speed} km/h")
    st.write(f"📊 Pressure: {pressure} hPa")

    # Weather Insights
    st.subheader("Atmospheric Insights")

    if humidity > 80:
        st.info("High humidity detected. Possibility of rainfall or cloudy conditions.")

    if temperature > 35:
        st.warning("High temperature levels detected.")

    if wind_speed > 30:
        st.warning("Strong wind conditions detected.")

    if pressure < 1000:
        st.info("Low atmospheric pressure may indicate unstable weather.")
