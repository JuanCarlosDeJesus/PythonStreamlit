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
st.markdown("<h1 style='text-align: center;'>User Registration Form</h1>", unsafe_allow_html=True)
# 2 ways to make a form
# 1 using the obj=st.from
# Create a form widget and using the dot "." you can add widgets to it
# st.write("Form - Creating a form Object")
# form=st.form("Form - Creating a form Object")
# form.text_input("First Name")
# form.form_submit_button("Submit")
# # 2 using the with st.form
# st.write("Form - Creating a form using with")
# with st.form("Form - Creating a with form"):
#     st.text_input("First Name")
#     st.form_submit_button("Submit")

# adding columns widget
# st.write("Form - Adding columns and getting user inputs")
with st.form("Form 1", clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    day,mon,yr=st.columns(3)
    day.text_input("Day")
    mon.text_input("Month")
    yr.text_input("Year")
    s_state=st.form_submit_button("Submit")

    if s_state:  # meaning the submit button was clicked
        if f_name == "" and l_name == "":
            st.warning("Please fill all information")
        else:
            st.success("Form information submitted successfully")
