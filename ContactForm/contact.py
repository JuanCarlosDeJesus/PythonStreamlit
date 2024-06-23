import streamlit as st

st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/carl.d3j3sus@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message Here"></textarea>
    <button type="submit">Send</button>
</form> 
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")