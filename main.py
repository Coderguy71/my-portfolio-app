import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/image.jpg", width=800)

with col2:
    st.title("Ishaan Trivedi")
    content = """
    Hi, I am Ishaan Trivedi! I am a Python and Java programmer, and a student at Morris Hill's Academy of Math, Science, 
    and Engineering.I am learning how to code in Python, and this is my portfolio website for all of my Python creations!
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium 
    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi
     architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur 
     aut odit aut fugit"""
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
       st.header(row['title'])
       st.write(row["description"])
       st.image("images/" + row['image'])
       st.write(f"[Source Code]({row['url']})")