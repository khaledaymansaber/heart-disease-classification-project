# 🧠 Heart Disease Prediction – End-to-End Data Science Workflow

This repository contains a complete Data Science workflow applied to a heart disease dataset. The goal is to explore, preprocess, analyze, and model the data to predict the presence of heart disease. The project follows a structured pipeline from raw data collection to model evaluation, visualization, and deployment.

---

## 📌 Project Overview

- **Problem Statement**: Predict the presence of heart disease based on clinical and demographic features.
- **Approach**: An end-to-end machine learning pipeline including:
  - Data acquisition & preprocessing
  - Balancing the dataset
  - Exploratory data analysis (EDA)
  - Feature engineering
  - Model building and evaluation
  - Web app deployment using Streamlit

---

## 🔍 Milestones

### 1. Data Collection
- Data sourced from a CSV file (can be extended via APIs or web scraping).
- Loaded using Pandas and inspected for relevant columns.

### 2. Preprocessing
- Selected only the required data points (balancing between 'Yes' and 'No' heart disease cases).
- Combined the two groups to form a balanced dataset.

### 3. Exploratory Data Analysis (EDA)
- Used `matplotlib`, `seaborn`, and `plotly` for rich interactive visualizations.
- Distribution analysis, correlation heatmaps, and categorical feature inspection.

### 4. Feature Engineering
- Encoded categorical variables.
- Scaled numerical features for optimal performance.

### 5. Model Development
- Applied different machine learning models such as:
  - Logistic Regression
  - Random Forest
- Evaluated using:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **Confusion Matrix**

> ✅ **Achieved test accuracy:** ~79% (on balanced dataset)

---

## 📊 Visualizations

- Interactive and static plots to visualize:
  - Class distributions
  - Feature relationships
  - Model performance metrics

---

## 🌐 Deployment

This project is deployed as a Streamlit web application, allowing users to interact with the model through a user-friendly interface.

### 🚀 Try it live:
👉 [Heart Disease Classification App](https://heart-disease-classification-project-1.streamlit.app/)

Users can:
- Input patient health data
- View prediction results instantly
- Understand feature impact on decision

---

## 🛠 Technologies Used

- Python
- Google Colab
- Pandas, NumPy
- Seaborn, Matplotlib, Plotly
- Scikit-learn
- Streamlit

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
