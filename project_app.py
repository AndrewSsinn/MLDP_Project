import streamlit as st
import joblib
import numpy as np

model = joblib.load('gradient_boosting_model.pkl')

gif_url = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTMxZ2xxNXF1cmgzb2JpNm5qYjhqdnNxdzR1cHc5NzdpaHJkZ29tbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5Zesu5VPNGJlm/giphy.gif'
st.image(gif_url, width=700)
st.title("💻 Ah Lim Laptop Price Predictions")
with st.sidebar:
    with st.expander("Laptop Specs ", expanded=True):
        brand = st.selectbox("Brand", ['Acer', 'Asus', 'Dell', 'HP', 'Lenovo'])
        speed = st.slider("Processor Speed (GHz)", 1.5, 4.0, step=0.1)
        ram = st.slider('RAM (GB)', 4, 32)
        storage = st.slider('Storage (GB)', 256, 1000)
        screen_size = st.slider('Screen Size (In)', 11.0, 17.0, step=0.1)
        weight = st.slider('Weight (KG)', 2.0, 5.0, step=0.1)

brand_columns = ['Brand_Acer', 'Brand_Asus', 'Brand_Dell', 'Brand_HP', 'Brand_Lenovo']
brand_input = [0] * len(brand_columns)
brand_input[brand_columns.index(f'Brand_{brand}')] = 1

input_data = np.array([speed, ram, storage, screen_size, weight,] + brand_input).reshape(1, -1)

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Price: ₽${prediction[0]:,.2f}")