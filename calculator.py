import streamlit as st

# Page Config
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Smart Calculator")

st.write("Simple Calculator using Streamlit")

st.divider()

# Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation
operation = st.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division"
    ]
)

# Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero not allowed")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result: {result}")

st.divider()

st.caption("Made with ❤️ using Streamlit")
