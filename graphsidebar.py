import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0,10,100)  # create a linspace object with number plots
st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4
{
    visibility: hidden;
}
.st-emotion-cache-1wbqy5l.e17vllj40
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
# adding the sidebar widget
st.sidebar.write("Hello, I am a sidebar!")
opt=st.sidebar.radio("Select any Graph:", options=("Line","Bar","H-Bar"))
# adding plot and graph widget
fig=plt.figure()  # create a figure() for the plots
plt.plot(x, np.sin(x))
st.write(fig)