import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Github: https://github.com/andfanilo/streamlit-lottie
# Lottie files: https://lottiefiles.com

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("lottiefiles/coding.json")
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

st.title("Include Lottie Files in Streamlit")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    # renderer="svg",
    height=None,
    width=None,
    key=None,
)
st_lottie(lottie_hello, key="Hello")