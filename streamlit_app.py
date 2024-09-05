import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from typing import List, Set
import re
from preprocessing import*

def chatbot():
        # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "you can ask me everything here, e.g. List 10 most valuable customers"}]

    # Display or clear chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # def clear_chat_history():
    #     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    # st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if 'filtered_df' not in st.session_state:
        st.session_state.filtered_df = None
    # mapping here, to find the answers
    if prompt := st.chat_input():
        response = find_mapped_keywords(prompt)
        if response is not None:
            st.session_state.filtered_df = response

    if st.session_state.filtered_df is not None:
        st.write(st.session_state.filtered_df)

def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    
    st.write("We have done visualization for these following questions")
    if st.button("Sales Prediction"):
        st.session_state["current_page"] = "Sales Prediction"
    if st.button("Churn Prediction"):
        st.session_state["current_page"] = "Churn Prediction"
    if st.button("Recommendation"):
        st.session_state["current_page"] = "Recommendation"

    chatbot()   
    

# an dashboard example, delete it when you finish designing other pages
def sales_dashboard():
    st.title("Sales Dashboard")
    st.write("Here is the interactive sales dashboard:")
    
    dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
    sales_data = np.random.randint(10000, 50000, size=(12,))
    sales_df = pd.DataFrame({'Date': dates, 'Sales': sales_data})

    fig = px.line(sales_df, x='Date', y='Sales', title='Interactive Monthly Sales for 2024')
    fig.update_traces(mode='lines+markers')

    st.plotly_chart(fig)

    if st.button("Go back to Home"):
        st.session_state["current_page"] = "home"

# default page
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# Navigation
if st.session_state["current_page"] == "home":
    home()
elif st.session_state["current_page"] == "Sales Prediction":
    sales_dashboard()