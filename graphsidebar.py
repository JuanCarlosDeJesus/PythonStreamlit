import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0,10,100)  # create a linspace object with number plots
b_x = np.array([1,2,3,4,5])
# adding the sidebar widget
opt=st.sidebar.radio("Select any Graph:", options=("Line","Bar","H-Bar"))
# adding plot and graph widget via the opt radio
if opt == "Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()  # create a figure() for the plots
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()  # create a figure() for the plots
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(b_x, b_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align:center;'>Horizontal Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()  # create a figure() for the plots
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(b_x*10, b_x)
    st.write(fig)