import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.jpg", width=600)

with col2:
    st.title("Ishaan Trivedi")
    content = """
    Hi, I am Ishaan Trivedi! I am a Python and Java programmer, and a student at Morris Hill's Academy of Math, Science, and Engineering.
    I am learning how to code in Python, and this is my portfolio website for all of my Python creations!"""
    st.info(content)