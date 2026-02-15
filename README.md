# 🌞 Solar Power Forecasting System

AI-Based Renewable Energy Output Prediction using Machine Learning.

---

## 📌 Overview

The **Solar Power Forecasting System** is a machine learning-based solution designed to predict solar power generation using environmental and atmospheric parameters.

Solar energy generation is highly dependent on weather conditions such as radiation, temperature, cloud cover, and solar angles. This project addresses the challenge of variability in renewable energy generation by developing a predictive model that improves grid planning and energy management.

The system demonstrates a complete end-to-end ML workflow including:

- Data preprocessing  
- Feature engineering  
- Model training  
- Performance evaluation  
- Web deployment using Streamlit  

---

## 🚀 Key Features

- 🌤 Predicts solar power output (kW)
- 📊 Feature importance analysis
- 📈 Performance evaluation using MAE & RMSE
- 🖥 Interactive Streamlit web interface
- ⚡ Real-time prediction simulation
- 🔍 Physics-aware feature selection

---

## 🧠 Machine Learning Approach

### 🔹 Algorithm Used
Random Forest Regressor

### 🔹 Why Random Forest?
- Handles non-linear relationships effectively  
- Reduces overfitting using ensemble learning  
- Works well with structured environmental data  
- Provides feature importance for explainability  

### 🔹 Input Features
- Shortwave Radiation  
- Temperature (2m above ground)  
- Relative Humidity  
- Wind Speed (10m above ground)  
- Total Cloud Cover  
- Angle of Incidence  
- Zenith  

### 🔹 Target Variable
- Generated Power (kW)

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| MAE | 532.03 |
| RMSE | 675.34 |
| Max Power | 3056 kW |

The model demonstrates strong predictive capability for solar energy forecasting and aligns with real-world solar physics factors.

---

## 📂 Project Structure
Solar_Power_Forecasting_System
│
├── data/
├── src/
│ └── train.py
├── models/ (ignored in Git)
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 🖥 Web Application

The project includes an interactive Streamlit application that:

- Accepts real-time environmental inputs
- Predicts solar power output
- Displays power visualization
- Shows feature importance analysis

---

## 📸 Application Screenshots

### 🌞 Prediction Dashboard
![Dashboard](https://github.com/rtanvi1604/Solar_Power_Forecasting_System/blob/5bad1713c9863062a866bd0fefd6b30fa3e4d153/Prediction_Dashboard.png)

### 🔍 Feature Importance Analysis
![Feature Importance](https://github.com/rtanvi1604/Solar_Power_Forecasting_System/blob/5bad1713c9863062a866bd0fefd6b30fa3e4d153/Feature_Analysis.png)

### 📈 Power Output Visualization
![Power Output](https://github.com/rtanvi1604/Solar_Power_Forecasting_System/blob/5bad1713c9863062a866bd0fefd6b30fa3e4d153/Power_Output_Visualization.png)

###  🔢 Detailed Input Parameters
![Input Parameters](https://github.com/rtanvi1604/Solar_Power_Forecasting_System/blob/5bad1713c9863062a866bd0fefd6b30fa3e4d153/Input_Parameters.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/rtanvi1604/Solar_Power_Forecasting_System.git
cd Solar_Power_Forecasting_System

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Train the Model
python src/train.py

### 4️⃣ Run the Web App
streamlit run app.py

---

## 🔮 Future Enhancements

- Implement LSTM for advanced time-series forecasting  
- Integrate real-time weather APIs  
- Deploy model on cloud platforms (Azure)  
- Extend to Hybrid Solar + Wind forecasting  
- Improve prediction accuracy through advanced tuning  

---

## 🌍 Impact

Accurate solar power forecasting enables:

- Improved grid stability  
- Reduced energy wastage  
- Better renewable energy planning  
- Support for sustainable smart cities  
- Contribution to carbon emission reduction  

---

## 📌 Note

The trained model file (`.pkl`) is not included in this repository due to GitHub file size limitations.  
Run `python src/train.py` to generate the model locally before launching the application.

---
