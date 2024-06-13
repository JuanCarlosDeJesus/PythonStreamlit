from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here: webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/41b08c2e-66e7-49d6-bfae-05ae89860138/ZTdTguFYDQ.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

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
    with right_column:
        st_lottie(lottie_coding, height = 300, key="coding")
    
    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Integrate Lottie animation inside your Streamlit App")
            st.write(
                    """
                    Learn how to use Lottie files in Streamlit!
                    Animations make our web app more engaging and fun, and lottie files are the easiest way to do it.
                    In this tutorial, I will show you exactly how to do it.
                    """
                     )
            st.markdown("[Watch video ... ](https://youtu.be/TXSOitgoINE)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("How To Add A Contact Form To Your Streamlit App")
            st.write(
                    """
                    Want to add a contact form to your Streamlit website?
                    In this video, I'm going to show you how to implement a contact form in your Strealit app using the free service 'Form Sumbit'.
                    """
                     )
            st.markdown("[Watch video ... ](https://youtu.be/FOULV9Xij_8)")
    
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/  !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/carl.d3j3sus@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()