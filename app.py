import streamlit as st
import pickle
import numpy as np
from datetime import datetime

# Load trained model
model = pickle.load(open('weather_model.pkl', 'rb'))

# Weather Labels
weather_labels = {
    0: "Cloudy ☁️",
    1: "Rainy 🌧️",
    2: "Sunny ☀️"
}

# Page Configuration
st.set_page_config(
    page_title="Weather Forecast Classification",
    page_icon="🌦️",
    layout="centered"
)

# Title
st.title("🌦️ Atmospheric Weather Classification System")

st.caption(
    "Machine Learning based atmospheric condition analysis system."
)

# Current Date & Time
current_time = datetime.now()

formatted_date = current_time.strftime("%d %B %Y")
formatted_time = current_time.strftime("%I:%M %p")

st.markdown(f"### 📅 Date: {formatted_date}")
st.markdown(f"### 🕒 Time: {formatted_time}")

st.divider()

# Description
st.write(
    """
    Predict weather conditions using atmospheric parameters
    such as temperature, humidity, wind speed, and pressure.
    """
)

# City Input
city = st.text_input(
    "📍 City Name",
    placeholder="Enter city name"
)

# Temperature Input
temperature = st.number_input(
    "🌡️ Temperature (°C)",
    min_value=-50.0,
    max_value=60.0,
    value=30.0
)

# Humidity Input
humidity = st.number_input(
    "💧 Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# Wind Speed Input
wind_speed = st.number_input(
    "🌬️ Wind Speed (km/h)",
    min_value=0.0,
    max_value=200.0,
    value=10.0
)

# Pressure Input
pressure = st.number_input(
    "📊 Pressure (hPa)",
    min_value=800.0,
    max_value=1200.0,
    value=1005.0
)

# Prediction Button
if st.button("Predict Weather"):

    # Prepare Input Data
    sample = np.array([
        [temperature, humidity, wind_speed, pressure]
    ])

    # Predict
    prediction = model.predict(sample)[0]

    # Weather Result
    weather = weather_labels.get(prediction, "Unknown")

    st.divider()

    # Main Prediction Output
    st.success(f"Predicted Weather Condition: {weather}")

    # Weather Report
    st.subheader("📋 Weather Analysis Report")

    st.write(f"📍 City: {city if city else 'Not Provided'}")
    st.write(f"📅 Date: {formatted_date}")
    st.write(f"🕒 Time: {formatted_time}")
    st.write(f"🌡️ Temperature: {temperature} °C")
    st.write(f"💧 Humidity: {humidity}%")
    st.write(f"🌬️ Wind Speed: {wind_speed} km/h")
    st.write(f"📊 Pressure: {pressure} hPa")

    st.divider()

    # Atmospheric Insights
    st.subheader("🔍 Atmospheric Insights")

    if humidity > 80:
        st.info(
            "High humidity levels detected. Possibility of rainfall or cloudy weather conditions."
        )

    if temperature > 35:
        st.warning(
            "High temperature conditions detected."
        )

    if wind_speed > 30:
        st.warning(
            "Strong wind conditions detected."
        )

    if pressure < 1000:
        st.info(
            "Low atmospheric pressure may indicate unstable weather patterns."
        )

    if (
        humidity <= 80 and
        temperature <= 35 and
        pressure >= 1000
    ):
        st.success(
            "Atmospheric conditions appear relatively stable."
        )
