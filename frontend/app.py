import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"




st.title("Expense Tracking System")

tab1,tab2 = st.tabs(["Add/Update","Analytics"])

with tab1:
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()

    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']

            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",
                                               label_visibility="collapsed")

            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{i}", label_visibility="collapsed")

            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expense updated successfully!")

            else:
                st.error("Failed to update expenses")

with tab2:
    col1,col2=st.columns(2)
    with col1:
        start_date=st.date_input("Start Date",datetime(2024,8,1))
    with col2:
        end_date=st.date_input("End Date",datetime(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/",json=payload)
        jsdata = response.json()

        dfdata={
            "Category":list(jsdata.keys()),
            "Total":[jsdata[category]['total'] for category in jsdata],
            "Percentage":[jsdata[category]['percentage'] for category in jsdata]
        }
        df = pd.DataFrame(dfdata)
        df_sorted=df.sort_values(by="Percentage",ascending=False)

        st.title("Expense Breakdown By Category")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"],width=0,height=0,use_container_width=True)

        df_sorted["Total"]=df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)



















