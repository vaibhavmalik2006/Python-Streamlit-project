import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Income & Expense Tracker", layout="centered")

st.title("💰 Income & Expense Tracker")

# Initialize session state for transactions
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# Sidebar for adding transactions
with st.sidebar:
    st.header("➕ Add Transaction")

    type_ = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.text_input("Category")
    description = st.text_input("Description (optional)")
    date = st.date_input("Date", value=datetime.today())

    if st.button("Add"):
        if amount > 0 and category:
            st.session_state.transactions.append({
                "Date": date,
                "Type": type_,
                "Amount": amount,
                "Category": category,
                "Description": description,
            })
            st.success("Transaction added!")
        else:
            st.warning("Please enter an amount and category.")

# Convert transactions to DataFrame
df = pd.DataFrame(st.session_state.transactions)

if not df.empty:
    # Summary
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense

    st.subheader("📊 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{income:,.2f}")
    col2.metric("Total Expense", f"₹{expense:,.2f}")
    col3.metric("Balance", f"₹{balance:,.2f}")

    # Show transaction history
    st.subheader("📋 Transaction History")
    st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)
else:
    st.info("No transactions yet. Add some from the sidebar!")

