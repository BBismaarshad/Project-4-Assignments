import streamlit as st

# App title with emoji
st.title("🧮 BMI Calculator")

# Add some spacing
st.write("")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    # User inputs with better labels
    height = st.slider("Height (cm)", 100, 250, 175, help="Adjust your height in centimeters")
    
with col2:
    weight = st.slider("Weight (kg)", 40, 200, 70, help="Adjust your weight in kilograms")

# Add some spacing
st.write("")

# Calculate BMI
bmi = weight / ((height/100) ** 2)

# Show result in a bigger font with color coding
if bmi < 18.5:
    bmi_color = "blue"
    category = "Underweight"
elif 18.5 <= bmi < 25:
    bmi_color = "green"
    category = "Healthy"
elif 25 <= bmi < 30:
    bmi_color = "orange"
    category = "Overweight"
else:
    bmi_color = "red"
    category = "Obese"

# Display BMI with colored highlight
st.markdown(f"""
### Your BMI: <span style='color:{bmi_color}; font-size:24px'>{bmi:.1f}</span>
### Category: <span style='color:{bmi_color}'>{category}</span>
""", unsafe_allow_html=True)

# Add some spacing
st.write("")

# BMI categories in an expandable section
with st.expander("BMI Categories Reference"):
    st.markdown("""
    - **Underweight**: Below 18.5
    - **Healthy**: 18.5 - 24.9
    - **Overweight**: 25 - 29.9
    - **Obese**: 30 or above
    """)

# Add some spacing
st.write("")

# Optional: Add a fun progress bar
st.progress(min(max(0, (bmi-15)/30), 1.0))
st.caption("BMI scale from 15 to 45")