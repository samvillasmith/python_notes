import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

st.write("Select your age")

age = st.slider("Select your age:", 0,100,25)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the dataframe
st.write("Here is the dataframe")
st.write(df)