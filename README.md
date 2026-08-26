# 🚌 Bus Travel Analytics

A Streamlit-based Bus Travel Analytics application that predicts bus travel time and provides analytics and insights based on historical trip data.

## 📌 Project Overview

The **Bus Travel Analytics** system analyzes historical bus trip data and predicts the expected travel time for a selected trip.

The application provides separate pages for trip input, travel-time prediction, analytics, insights, and prediction history.

## ✨ Features

- 📝 Enter trip details
- ⏱️ Predict bus travel time
- 📊 Analyze historical travel data
- 💡 Generate travel insights
- 📜 View prediction history
- 🚌 Support for different bus terminals and travel directions
- 📈 Interactive Streamlit dashboard

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Machine Learning
- CSV Dataset

## 📂 Project Structure

```text
bus-travel-analytics/
│
├── bus_app.py
├── bus_trips_654.csv
├── requirements.txt
├── .gitignore
│
└── pages/
    ├── 1_Trip_Input.py
    ├── 2_Prediction.py
    ├── 3_Analytics.py
    ├── 4_Insights.py
    └── 5_Prediction_History.py
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sushmitharaja-data/bus-travel-analytics.git
```

### 2. Open the project folder

```bash
cd bus-travel-analytics
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run bus_app.py
```

## 📊 Dataset

The project uses `bus_trips_654.csv`, which contains historical bus trip information used for travel-time analysis and prediction.

## 🎯 Objective

The main objective of this project is to use historical bus travel data and machine learning techniques to estimate travel time and provide useful analytics for better understanding of bus transportation patterns.

## 👩‍💻 Author

**Sushmitha Raja**

GitHub: https://github.com/sushmitharaja-data
