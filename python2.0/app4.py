import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set page title
st.set_page_config(page_title="Expense Tracker", layout="centered")

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

st.title("💰 Expense Tracker")

# --- Input form to add expenses ---
with st.form("expense_form"):
    st.subheader("Add a New Expense")
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Utilities", "Other"])
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
    with col2:
        date = st.date_input("Date", value=datetime.today())
        description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")
    if submitted:
        new_expense = {
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        st.session_state.expenses = pd.concat(
            [st.session_state.expenses, pd.DataFrame([new_expense])],
            ignore_index=True
        )
        st.success("Expense added!")

# --- Display expenses ---
st.subheader("All Expenses")
st.dataframe(st.session_state.expenses)

# --- Summary ---
st.subheader("Summary")

if not st.session_state.expenses.empty:
    total = st.session_state.expenses["Amount"].sum()
    st.metric("Total Spent", f"${total:.2f}")

    # --- Pie chart of categories ---
    category_totals = st.session_state.expenses.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.info("No expenses recorded yet.")

# Optional: Save data to CSV (session only)
if st.download_button("Download as CSV", data=st.session_state.expenses.to_csv(index=False), file_name="expenses.csv"):
    st.success("Download started.")
