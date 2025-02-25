import streamlit as st

# Conversion Categories
conversion_categories = {
    "Length": ["Meter to Foot", "Meter to Inch", "Meter to Mile", "Meter to Kilometer"],
    "Weight": ["Kilogram to Pound", "Pound to Kilogram", "Kilogram to Ounce"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
    "Time": ["Second to Minute", "Minute to Second", "Second to Hour", "Hour to Second", "Minute to Hour", "Hour to Minute"]
}

# Streamlit UI
st.title("Unit Converter")

# Category selection
category = st.selectbox("Choose a conversion category:", list(conversion_categories.keys()))

# Conversion type selection
conversion_type = st.selectbox("Choose conversion type:", conversion_categories[category])

# User input value
value = st.number_input(f"Enter the value to convert ({conversion_type.split(' to ')[0]}):", min_value=0.0, format="%.4f")

# Conversion logic
def convert_value(category, conversion_type, value):
    if category == "Length":
        conversions = {
            "Meter to Foot": value * 3.28084,
            "Meter to Inch": value * 39.3701,
            "Meter to Mile": value / 1609.34,
            "Meter to Kilometer": value / 1000,
        }
    elif category == "Weight":
        conversions = {
            "Kilogram to Pound": value * 2.20462,
            "Pound to Kilogram": value / 2.20462,
            "Kilogram to Ounce": value * 35.274
        }
    elif category == "Temperature":
        conversions = {
            "Celsius to Fahrenheit": (value * 9/5) + 32,
            "Fahrenheit to Celsius": (value - 32) * 5/9
        }
    elif category == "Time":
        conversions = {
            "Second to Minute": value / 60,
            "Minute to Second": value * 60,
            "Second to Hour": value / 3600,
            "Hour to Second": value * 3600,
            "Minute to Hour": value / 60,
            "Hour to Minute": value * 60
        }
    return conversions.get(conversion_type, "Invalid Conversion")

# Convert button
if st.button("Convert"):
    result = convert_value(category, conversion_type, value)
    st.success(f"Converted Value: {result:.4f} {conversion_type.split(' to ')[1]}")
