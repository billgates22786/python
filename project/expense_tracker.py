# expense_tracker.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Personal Expense Tracker")

# Initialize CSV file
FILE = "expenses.csv"

# Load or create data
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

# Input section
st.subheader("Add a New Expense")
date = st.date_input("Date")
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")

if st.button("Add Expense"):
    new_expense = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(FILE, index=False)
    st.success("Expense added!")

# Display data
st.subheader("All Expenses")
st.dataframe(df)

# Visualization
st.subheader("Expense Summary")

if not df.empty:
    # Category-wise total
    cat_sum = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    cat_sum.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    plt.title("Spending by Category")
    st.pyplot(fig)

    # Trend over time
    df["Date"] = pd.to_datetime(df["Date"])
    daily_sum = df.groupby("Date")["Amount"].sum()

    fig2, ax2 = plt.subplots()
    daily_sum.plot(kind='line', marker='o', ax=ax2)
    plt.title("Spending Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Amount (₹)")
    st.pyplot(fig2)
