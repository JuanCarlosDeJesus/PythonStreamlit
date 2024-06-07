import streamlit as st

# find more emojis here: webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Carl :wave:")
    st.title("A Python Developer from the US")
    st.write("I am using python and VBA to more efficient in data analysis")
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            On my WebPage I am creating content for people who:
            - are looking to add to their Python knowledge
            - are looking for ways to use Python to reduce repetitive tasks
            - are looking to use Python for Data science and Analysis

            If this sounds interesting to you, consider sticking around
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")