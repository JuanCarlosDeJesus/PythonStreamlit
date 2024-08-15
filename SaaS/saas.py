import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("My First SaaS! :rocket:")

add_auth(required=True)

# AUTHENTICATION + SUBSCRIPTION
# EMAIL INFO STORED
st.write(f"Subscription Status: {st.session_state.user_subscribe}")
st.write("💐 Yay! You're all set and subscribed! 💐")
st.write(f"By the way, your email is: {st.session_state.email}")