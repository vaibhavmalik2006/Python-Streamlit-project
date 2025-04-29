import streamlit as st
import pandas as pd
import numpy as np


# App title
st.title("🧮 BMI Calculator")

# Input fields
st.header("Enter your details:")
height = st.number_input("Height (in centimeters)", min_value=50.0, max_value=300.0, value=170.0)
weight = st.number_input("Weight (in kilograms)", min_value=10.0, max_value=300.0, value=70.0)

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height / 100  # convert height to meters
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    # Interpretation
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")


