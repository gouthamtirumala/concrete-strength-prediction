import streamlit as st
import numpy as np
import pickle

# Load the trained model
model_filename = 'concrete_strength_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Display the image at the top
st.image(r"inoopng.png")
st.image(r"concrete.png.png", width=500)

# Title of the app
st.title('Concrete Strength Prediction')

# Create columns for layout
col1, col2 = st.columns(2)  # Two columns for a more compact layout

with col1:
    cement = st.number_input('Cement (kg/m³)', min_value=0.0, max_value=540.0, value=273.0)
    slag = st.number_input('Blast Furnace Slag (kg/m³)', min_value=0.0, max_value=359.4, value=179.7)
    fly_ash = st.number_input('Fly Ash (kg/m³)', min_value=0.0, max_value=200.1, value=100.05)
    water = st.number_input('Water (kg/m³)', min_value=0.0, max_value=247.0, value=123.5)

with col2:
    superplasticizer = st.number_input('Superplasticizer (kg/m³)', min_value=0.0, max_value=32.0, value=16.0)
    coarse_aggregate = st.number_input('Coarse Aggregate (kg/m³)', min_value=800.0, max_value=1145.0, value=972.5)
    fine_aggregate = st.number_input('Fine Aggregate (kg/m³)', min_value=594.0, max_value=992.6, value=793.3)
    age = st.number_input('Age (days)', min_value=1, max_value=365, value=28)

# Create an input array for prediction
input_values = np.array([[cement, slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]])

# Make a prediction
if st.button("Submit"):
    predicted_strength = model.predict(input_values)
    st.write(f'Predicted Concrete Strength: {predicted_strength[0]:.2f} MPa')
    st.write('**Note:** The predicted concrete strength is based on theoretical calculations. Actual concrete strength may vary due to practical uncertainties, such as material quality, mixing accuracy, and environmental conditions.')
