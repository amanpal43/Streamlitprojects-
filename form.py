import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Information Form",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Information Form")

st.write("Fill all details carefully.")

st.divider()

# Name Input
name = st.text_input("Enter your name")

# Age Input
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    step=1
)

# Course Selection
course = st.selectbox(
    "Select Course",
    ["BCA", "BBA", "MBA", "MCA"]
)

# Gender Selection
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

# Skills Selection
skills = st.multiselect(
    "Select your skills",
    ["Python", "Java", "C++", "AI", "Machine Learning"]
)

# Marks Slider
marks = st.slider(
    "Enter Marks",
    0, 100
)

# Terms Checkbox
agree = st.checkbox("I agree to the terms and conditions")

# Submit Button
if st.button("Submit"):

    if name == "":
        st.warning("⚠ Please enter your name")

    elif not agree:
        st.error("❌ Please accept terms and conditions")

    else:
        st.success("✅ Form Submitted Successfully!")

        st.subheader("Student Details")

        st.write("👤 Name:", name)
        st.write("🎂 Age:", age)
        st.write("📘 Course:", course)
        st.write("⚧ Gender:", gender)
        st.write("💻 Skills:", ", ".join(skills))
        st.write("📊 Marks:", marks)

st.divider()

st.caption("Made with ❤️ using Streamlit")
