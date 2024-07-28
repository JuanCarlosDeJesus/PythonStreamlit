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