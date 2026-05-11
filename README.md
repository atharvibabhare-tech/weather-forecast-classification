# Weather Prediction ML Project

A machine learning-based weather prediction system developed using Python and Scikit-learn.  
This project analyzes atmospheric conditions and predicts weather classifications using supervised machine learning algorithms.

---

## Project Overview

This project focuses on building a weather classification model capable of predicting weather conditions based on multiple environmental parameters such as:

- Temperature
- Humidity
- Wind Speed
- Atmospheric Pressure

The workflow includes:
- Data preprocessing
- Feature engineering
- Label encoding
- Model training
- Prediction
- Performance evaluation

The project demonstrates an end-to-end machine learning pipeline for weather analytics and forecasting applications.

---

## Features

- Weather condition prediction system
- Data preprocessing and cleaning
- Feature engineering from raw weather data
- Classification model implementation
- Decision Tree and Random Forest support
- Model accuracy evaluation
- Manual input prediction system
- Streamlit-ready deployment structure

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning |
| Matplotlib | Data visualization |
| Streamlit | Web app deployment |

---

## Machine Learning Workflow

### 1. Data Collection
Weather-related parameters were collected and organized into a structured dataset.

### 2. Data Preprocessing
- Datetime formatting
- Feature selection
- Label encoding
- Data cleaning

### 3. Feature Engineering
Additional meaningful features were extracted to improve model learning capability.

### 4. Model Training
Classification algorithms were trained on processed weather data.

### 5. Model Evaluation
Performance metrics such as accuracy and classification analysis were used to evaluate the model.

---

## Input Features

The model uses the following input features:

- Temperature
- Humidity
- Wind Speed
- Pressure

Example:

```python
sample = [[36, 85, 12, 1005]]
```

---

## Prediction Example

```python
result = model.predict(sample)

print(le_weather.inverse_transform(result))
```

Example Output:

```text
['Rainy']
```

---

## Project Structure

```text
weather-prediction-ml/
│
├── app.py
├── weather_prediction.ipynb
├── weather_model.pkl
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-prediction-ml.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook or Streamlit app.

---

## Streamlit Deployment

To run the Streamlit application locally:

```bash
streamlit run app.py
```

---

## Future Improvements

- Integration with real-time weather APIs
- Advanced forecasting models
- Time-series prediction
- Deep learning implementation
- Interactive dashboards
- Cloud deployment

---

## Applications

- Weather analytics
- Forecasting systems
- Environmental monitoring
- Machine learning research
- Predictive analytics projects

---

## Author

Developed as a machine learning and predictive analytics project using Python and Scikit-learn.
