import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go # Import Plotly

# Set page configuration for a wider layout and a title
st.set_page_config(layout="centered", page_title="Air Quality Predictor")

# --- Custom CSS for enhanced aesthetics ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #333333;
    }

    body {
        background-color: #f0f2f6; /* Light gray background */
    }

    .stApp {
        background-color: #f0f2f6; /* Ensure the main app area matches */
    }

    /* Header styling */
    .stApp > header {
        background-color: #f0f2f6;
    }

    div.stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 25px; /* More rounded */
        cursor: pointer;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        width: 100%; /* Make button span full width of its container */
    }

    div.stButton > button:hover {
        background-color: #45a049; /* Darker green on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }

    /* Input field styling */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #cccccc;
        padding: 10px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: border-color 0.3s ease;
    }

    .stNumberInput > div > div > input:focus {
        border-color: #4CAF50;
        outline: none;
        box-shadow: 0 0 0 0.2rem rgba(76, 175, 80, 0.25);
    }

    /* General container styling for sections */
    .stAlert, .stInfo, .stSuccess, .stWarning, .stError {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .stAlert { background-color: #fff3cd; color: #856404; border-color: #ffeeba; } /* Warning */
    .stInfo { background-color: #d1ecf1; color: #0c5460; border-color: #bee5eb; } /* Info */
    .stSuccess { background-color: #d4edda; color: #155724; border-color: #c3e6cb; } /* Success */
    .stWarning { background-color: #fff3cd; color: #856404; border-color: #ffeeba; } /* Warning */
    .stError { background-color: #f8d7da; color: #721c24; border-color: #f5c6cb; } /* Error */


    /* Custom styling for the main content blocks to give them a card-like appearance */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        background-color: #ffffff; /* White background for content blocks */
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Specific styling for the header div */
    div[data-testid="stMarkdownContainer"] h1 {
        color: #333333;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 0.5em;
    }

    /* Subheader styling */
    h2 {
        color: #4CAF50;
        font-weight: 600;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    /* Horizontal rule styling */
    hr {
        border-top: 2px solid #e0e0e0;
        margin: 2rem 0;
    }

    /* Footer styling */
    .footer-text {
        text-align: center;
        color: #888888;
        font-size: 0.9em;
        margin-top: 30px;
    }

    /* Responsive adjustments for columns */
    @media (max-width: 768px) {
        .st-cq { /* Targets Streamlit columns */
            flex-direction: column;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Load the model ---
try:
    # Assuming 'li.pkl' is in the same directory or a known path
    with open('li.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Model file 'li.pkl' not found. Please ensure it's in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# --- Header Section ---
st.markdown(
    """
    <div style="background-color:#ffffff;padding:15px;border-radius:10px;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h1 style="color:#333333;text-align:center;">💨 Air Quality Index (AQI) Predictor 💨</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("") # Add some space

st.info(
    """
    The **Air Quality Index (AQI)** is a crucial tool for understanding air pollution levels and their potential
    health impacts. Lower AQI values indicate cleaner air, while higher values signify more serious pollution.
    Use this predictor to estimate the AQI based on various pollutant concentrations.
    """
)

st.write("---") # Horizontal line for separation

# --- Input Section ---
st.subheader("📊 Enter Pollutant Levels")
st.markdown("Please input the concentrations of the following air pollutants:")

# Use columns for a more organized input layout
col1, col2 = st.columns(2)

with col1:
    pm1 = st.number_input("Particulate Matter 1 (PM1 - µg/m³)", min_value=0.0, help="Concentration of particulate matter less than 1 micrometer in diameter.")
    pm2 = st.number_input("Particulate Matter 2.5 (PM2.5 - µg/m³)", min_value=0.0, help="Concentration of particulate matter less than 2.5 micrometers in diameter.")
    no2 = st.number_input("Nitrogen Dioxide (NO₂ - ppb)", min_value=0.0, help="Concentration of Nitrogen Dioxide.")

with col2:
    so2 = st.number_input("Sulfur Dioxide (SO₂ - ppb)", min_value=0.0, help="Concentration of Sulfur Dioxide.")
    co = st.number_input("Carbon Monoxide (CO - ppm)", min_value=0.0, help="Concentration of Carbon Monoxide.")
    o3 = st.number_input("Ozone (O₃ - ppb)", min_value=0.0, help="Concentration of Ozone.")

st.write("---")

# --- Prediction Button and Output ---
if st.button("✨ Get AQI Prediction ✨", help="Click to predict the Air Quality Index based on your inputs."):
    if pm1 is None or pm2 is None or no2 is None or so2 is None or co is None or o3 is None:
        st.warning("Please enter values for all pollutant fields before predicting.")
    else:
        # Prepare input features for the model
        input_features = np.array([[pm1, pm2, no2, so2, co, o3]])

        # Make prediction
        try:
            prediction = model.predict(input_features)
            aqi_value = prediction[0]

            st.subheader("🔮 Your Predicted AQI")

            # Display prediction with a colored box based on AQI level
            if aqi_value <= 50:
                st.success(f"### AQI: {aqi_value:.2f} - Good (🟢)")
                st.markdown("Air quality is considered satisfactory, and air pollution poses little or no risk.")
                meter_color = "green"
            elif aqi_value <= 100:
                st.warning(f"### AQI: {aqi_value:.2f} - Moderate (🟡)")
                st.markdown("Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.")
                meter_color = "gold" # Changed from yellow for better contrast
            elif aqi_value <= 150:
                st.error(f"### AQI: {aqi_value:.2f} - Unhealthy for Sensitive Groups (🟠)")
                st.markdown("Members of sensitive groups may experience health effects. The general public is less likely to be affected.")
                meter_color = "orange"
            elif aqi_value <= 200:
                st.error(f"### AQI: {aqi_value:.2f} - Unhealthy (🔴)")
                st.markdown("Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.")
                meter_color = "red"
            else:
                st.error(f"### AQI: {aqi_value:.2f} - Very Unhealthy or Hazardous (🟣 / 🟤)")
                st.markdown("Health warnings of emergency conditions. The entire population is more likely to be affected.")
                meter_color = "darkred" # Using darkred for hazardous

            # --- Plotly Gauge Meter ---
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = min(aqi_value, 500), # Cap value at 500 for meter scale
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Air Quality Index (AQI)"},
                gauge = {
                    'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': meter_color}, # Color of the main bar
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 50], 'color': "lightgreen", 'name': 'Good'},
                        {'range': [51, 100], 'color': "gold", 'name': 'Moderate'}, # Changed to gold
                        {'range': [101, 150], 'color': "orange", 'name': 'Unhealthy for Sensitive Groups'},
                        {'range': [151, 200], 'color': "red", 'name': 'Unhealthy'},
                        {'range': [201, 300], 'color': "purple", 'name': 'Very Unhealthy'},
                        {'range': [301, 500], 'color': "darkred", 'name': 'Hazardous'}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': aqi_value # Mark the predicted value
                    }
                }
            ))

            fig.update_layout(
                paper_bgcolor="white", # Background color of the entire figure
                font_color="black",
                height=300, # Adjust height
                margin=dict(l=20, r=20, b=20, t=20) # Adjust margins
            )

            st.plotly_chart(fig, use_container_width=True) # Display the Plotly chart

            st.balloons() # Add a celebratory animation
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

st.write("---")

# --- Footer ---
st.markdown(
    """
    <p class="footer-text">
    Designed by Indrajith & Devadath — Delivering data-driven insights for a healthier environment.
    </p>
    """,
    unsafe_allow_html=True
)
