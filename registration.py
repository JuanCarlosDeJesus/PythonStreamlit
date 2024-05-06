import streamlit as st

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
st.markdown("<h1>User Registration Form</h1>", unsafe_allow_html=True)
# 2 ways to make a form
# 1 using the obj=st.from
# Create a form widget and using the dot "." you can add widgets to it
st.write("Form - Creating a form Object")
form=st.form("Form - Creating a form Object")
form.text_input("First Name")
form.form_submit_button("Submit")
# 2 using the with st.form
st.write("Form - Creating a form using with")
with st.form("Form - Creating a with form"):
    st.text_input("First Name")
    st.form_submit_button("Submit")

# adding columns widget
st.write("Form - Adding columns")
with st.form("Form - Columns a with form"):
    col1,col2=st.columns(2)
    col1.text_input("First Name")
    col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.form_submit_button("Submit")
