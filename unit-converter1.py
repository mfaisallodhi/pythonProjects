import streamlit as st
     

def convert_units(value, unit_from, unit_to):
    
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000 
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("🌍Unit Converter🌍")

value = st.number_input("Enter the value:")

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

    
if st.button("Convert"):
   result = convert_units(value, unit_from, unit_to)
   st.write(f"Convert value: {result}")
    