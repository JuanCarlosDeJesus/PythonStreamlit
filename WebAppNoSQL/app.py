import calendar
from datetime import datetime

import streamlit as st
import plotly.graph_objects as go


# ----------- SETTINGS -----------
incomes = ["Salary","Blog","Other Income"]
expenses = ["Rent","Utilities","Groceries","Car","Other Expenses","Saving"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:" # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# ---------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1] # this year and next
months = list(calendar.month_name[1:])

# --- INPUT AND SAVE PERIODS ---
st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key="month")
    col2.selectbox("Select Year:", years, key="year")

    "---"
    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment here...")

    "---"
    submitted = st.form_submit_button("Saved Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        # TODO: Insert values into database
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.success("Data Saved!")


# --- PLOT PERIODS ---
st.header("Data Visualization")
with st.form("saved_periods"):
    # TODO: Get periods from database
    period = st.selectbox("Select Period:", ["2024_March"])
    submitted = st.form_submit_button("Plot Period")
    if submitted:
        # TODO: Get data from database
        comment = "Some comment"
        incomes = {'Salary': 1500, 'Blog': 50, 'Other Income': 10}
        expenses = {'Rent': 600, 'Utilities': 200, 'Groceries': 300, 'Car': 100, 'Other Expenses': 50, 'Savings': 10}

        # Create metrics
        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remaining_budget = total_income - total_expense
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"{total_income} {currency}")
        col2.metric("Total Expense", f"{total_expense} {currency}")
        col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
        st.text(f"Comment: {comment}")

        # Create sankey chart
        label = list(incomes.keys()) + ["Total Income"]