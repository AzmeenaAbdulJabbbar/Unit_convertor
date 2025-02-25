# Unit Converter

This is a simple **Unit Converter** web app built using **Streamlit**. The app allows users to convert different units of measurement, including Length, Weight, Temperature, and Time.

## Features
- **Convert Length Units**: Meter to Foot, Meter to Inch, Meter to Mile, Meter to Kilometer
- **Convert Weight Units**: Kilogram to Pound, Pound to Kilogram, Kilogram to Ounce
- **Convert Temperature Units**: Celsius to Fahrenheit, Fahrenheit to Celsius
- **Convert Time Units**: Second to Minute, Minute to Second, Second to Hour, Hour to Second, Minute to Hour, Hour to Minute
- **User-Friendly Interface**: Dropdown selections, real-time input, and conversion results
- **Hover Effect**: Custom CSS applied for better UI experience

## Installation
To run the application locally, follow these steps:

### Prerequisites
Make sure you have Python installed on your system. You also need to install **Streamlit**:
```sh
pip install streamlit
```

### Run the Application
Clone the repository (or save the script) and navigate to the directory, then run:
```sh
streamlit run app.py
```

## Usage
1. Select a **conversion category** (Length, Weight, Temperature, Time)
2. Choose a **conversion type** (e.g., Meter to Foot)
3. Enter the value to convert
4. Click the **Convert** button to see the result

## Customization
- You can add more conversions in the `conversion_categories` dictionary
- Modify the UI using Streamlit's markdown and custom CSS

## License
This project is open-source and available for modification and distribution.

## Author
Developed with ❤️ using Streamlit.

