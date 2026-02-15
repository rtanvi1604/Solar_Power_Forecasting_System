import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Solar Power Forecasting System",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Main title styling */
    .main-title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #f6d365 0%, #fda085 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        padding: 1rem 0 !important;
        text-align: center !important;
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.2rem !important;
        color: #666 !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
        margin: 2rem 0 1rem 0 !important;
        padding-bottom: 0.5rem !important;
        border-bottom: 3px solid #f6d365 !important;
    }
    
    /* Info box styling */
    .info-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #f6d365;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-top: 3rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #f6d365 0%, #fda085 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 5px;
        width: 100%;
        transition: transform 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    .sidebar-header {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
        padding: 1rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("models/solar_model.pkl")

model = load_model()

st.markdown('<h1 class="main-title">☀️ Solar Power Forecasting System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Renewable Energy Prediction Platform</p>', unsafe_allow_html=True)

current_time = datetime.now().strftime("%B %d, %Y - %I:%M %p")
st.markdown(f"<div style='text-align: right; color: #666;'>{current_time}</div>", unsafe_allow_html=True)


with st.sidebar:
    st.markdown('<p class="sidebar-header">⚙️ Input Parameters</p>', unsafe_allow_html=True)
    
    with st.expander("🌡️ Weather Parameters", expanded=True):
        radiation = st.slider("Shortwave Radiation (W/m²)", 0.0, 1200.0, 100.0, 
                             help="Solar radiation received on the surface")
        temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0,
                               help="Ambient temperature")
        humidity = st.slider("Relative Humidity (%)", 0.0, 100.0, 50.0,
                            help="Relative humidity at 2m above ground")
        wind_speed = st.slider("Wind Speed (m/s)", 0.0, 30.0, 5.0,
                              help="Wind speed at 10m above ground")
    
    with st.expander("☁️ Cloud & Solar Parameters", expanded=True):
        cloud_cover = st.slider("Total Cloud Cover (%)", 0.0, 100.0, 20.0,
                               help="Percentage of sky covered by clouds")
        incidence = st.slider("Angle of Incidence (°)", 0.0, 90.0, 30.0,
                             help="Angle between sun rays and solar panel")
        zenith = st.slider("Solar Zenith Angle (°)", 0.0, 90.0, 30.0,
                          help="Angle between sun and vertical direction")
    
    st.markdown("---")
    
    st.markdown("""
    <div style='background-color: #e1f5fe; padding: 1rem; border-radius: 5px;'>
        <h4 style='color: #01579b; margin: 0;'>Plant Information</h4>
        <p style='color: #0277bd; margin: 0.5rem 0 0 0;'>
            Installed Capacity: 3056.79 kW<br>
            Optimal Range: 1500-2500 kW
        </p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button("🚀 Generate Forecast", use_container_width=True)

if predict_button:
    
    input_data = np.array([[radiation,
                            temperature,
                            humidity,
                            wind_speed,
                            cloud_cover,
                            incidence,
                            zenith]])
    
    with st.spinner("Calculating solar power forecast..."):
        prediction = model.predict(input_data)[0]
        efficiency = (prediction / 3056.79) * 100
    
    st.markdown('<h2 class="section-header">📊 Prediction Results</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <div class="metric-label">Predicted Power</div>
            <div class="metric-value">{prediction:.2f} kW</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        plant_status = "Optimal" if efficiency > 50 else "Sub-optimal"
        color = "background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);" if efficiency > 50 else "background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);"
        st.markdown(f"""
        <div class="metric-card" style="{color}">
            <div class="metric-label">Plant Utilization</div>
            <div class="metric-value">{efficiency:.2f}%</div>
            <div style="font-size: 0.9rem; margin-top: 0.5rem;">Status: {plant_status}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        co2_saved = prediction * 0.0007  
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);">
            <div class="metric-label">CO₂ Savings</div>
            <div class="metric-value">{co2_saved:.2f} kg</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        homes_powered = prediction / 30  
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);">
            <div class="metric-label">Homes Powered</div>
            <div class="metric-value">{homes_powered:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">📈 Power Output Visualization</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prediction,
            title = {'text': "Current Power Output (kW)"},
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge = {
                'axis': {'range': [0, 3056.79]},
                'bar': {'color': "#f6d365"},
                'steps': [
                    {'range': [0, 1000], 'color': "#ffcccc"},
                    {'range': [1000, 2000], 'color': "#ffffcc"},
                    {'range': [2000, 3056.79], 'color': "#ccffcc"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 3056.79
                }
            }
        ))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col2:
        categories = ['Radiation', 'Temperature', 'Humidity', 'Wind Speed', 'Cloud Cover']
        values = [radiation/12, temperature/5, humidity/10, wind_speed*3.33, 100-cloud_cover]
        
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            marker=dict(color="#f6d365")
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            height=300,
            title="Input Parameters Overview"
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    st.markdown('<h2 class="section-header">🔍 Feature Importance Analysis</h2>', unsafe_allow_html=True)
    
    importances = model.feature_importances_
    features = [
        "Radiation",
        "Temperature",
        "Humidity",
        "Wind Speed",
        "Cloud Cover",
        "Angle of Incidence",
        "Zenith"
    ]
    
    importance_df = pd.DataFrame({
        'Feature': features,
        'Importance': importances
    }).sort_values('Importance', ascending=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig_importance = px.bar(importance_df, 
                                x='Importance', 
                                y='Feature',
                                orientation='h',
                                title="Feature Importance in Model",
                                color='Importance',
                                color_continuous_scale='viridis')
        fig_importance.update_layout(height=400)
        st.plotly_chart(fig_importance, use_container_width=True)
    
    with col2:
        top_feature = importance_df.iloc[-1]['Feature']
        top_importance = importance_df.iloc[-1]['Importance'] * 100
        
        st.markdown("""
        <div class="info-box">
            <h4 style='color: #2c3e50; margin-top: 0;'>📊 Key Insights</h4>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <ul style='color: #666;'>
            <li><b>Most Important Feature:</b> {top_feature}</li>
            <li><b>Contribution:</b> {top_importance:.1f}%</li>
            <li><b>Model Type:</b> Random Forest Regressor</li>
            <li><b>Estimation:</b> High Confidence</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background-color: #e8f5e8; padding: 1rem; border-radius: 5px; margin-top: 1rem;'>
            <h5 style='color: #2e7d32; margin: 0;'>💡 Tip</h5>
            <p style='color: #1b5e20; margin: 0.5rem 0 0 0;'>
                Higher radiation and optimal temperature generally lead to better power output.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("📋 Detailed Input Parameters", expanded=False):
        input_df = pd.DataFrame({
            'Parameter': ['Radiation (W/m²)', 'Temperature (°C)', 'Humidity (%)', 
                         'Wind Speed (m/s)', 'Cloud Cover (%)', 'Incidence Angle (°)', 'Zenith (°)'],
            'Value': [radiation, temperature, humidity, wind_speed, cloud_cover, incidence, zenith],
            'Optimal Range': ['400-800', '20-30', '40-60', '3-8', '0-30', '0-45', '0-45']
        })
        st.dataframe(input_df, use_container_width=True)

else:
    st.markdown('<h2 class="section-header">👋 Welcome to Solar Power Forecasting</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <h3 style='color: #2c3e50;'>How It Works</h3>
            <ol style='color: #666; line-height: 1.8;'>
                <li>Adjust input parameters in the sidebar</li>
                <li>Click "Generate Forecast" to predict power output</li>
                <li>View detailed analytics and visualizations</li>
                <li>Get insights about plant performance</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <h3 style='color: #2c3e50;'>Key Features</h3>
            <ul style='color: #666; line-height: 1.8;'>
                <li>Real-time solar power prediction</li>
                <li>Interactive parameter adjustment</li>
                <li>Feature importance analysis</li>
                <li>Environmental impact metrics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <img src="https://img.icons8.com/fluency/96/000000/solar-panel.png"/>
        <p style='color: #666;'>Adjust parameters and click "Generate Forecast" to start</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h4>Developed by Tanvi R</h4>
    <p>Renewable Energy ML Internship Project | © 2025</p>
    <p style='font-size: 0.8rem; margin-top: 1rem;'>
        This system uses Machine Learning to predict solar power generation based on weather and solar parameters.
    </p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)