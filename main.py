import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png")


with col2:
    st.title("Rad Hoda")
    content = """
    Hi, I am Rad! I am a Software Engineering Student at University of 
    Washington Bothell. I am aiming to graduate in 2024, and have a 
    passion for Machine Learning and Data Science. 
    """

    st.info(content)

    st.write("Below you can find some of the apps I have built with Python and C++."
             "Feel free to contact me!")

    
col3, col4 = st.columns(2)

df = pandas.read_csv(r"data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
