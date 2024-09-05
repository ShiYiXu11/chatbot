import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from typing import List, Set
import re
import streamlit as st
import pandas as pd
import requests
import random
import string
from io import StringIO

dataset_keywords = {
        'customer': ['customer', 'valuable customers', 'top customers'],
        'product': ['product', 'frequent product', 'buy product'],
        'sale': ["sale","demand","return"],
        'robot language':['&','#','?','^']
    }
matched_dataset=0

# ignore this, we can't show dashbpards in dialogue, will choose another way
# def filtered_data(df):

#     st.title('Table')
   
#     # 条件选择器
#     selected_cus = st.selectbox('Customer Segment:', df['Customer_Segment'].unique())
#     selected_article = st.multiselect('ArticleID:', df['ArticleID'].unique())
#     if selected_cus and selected_article:
#         filtered_df = df[(df['Customer_Segment'] == selected_cus) & (df['ArticleID'].isin(selected_article))]
#         return filtered_df
#     else:
#         st.write("Please select both Customer Segment and ArticleID.")
#         return None
def generate_random_string(length):
    """Generates a random string of the specified length."""
    # Combine letters, digits, and punctuation to create randomness
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def find_mapped_keywords(customer_request: str) -> Set[str]:
    """
    Finds keywords from the customer request that exist in the predefined question keywords list.
    
    :param customer_request: The text input from the customer.
    :param question_keywords: A list of predefined keywords to match against.
    :return: A set of keywords found in both customer request and question keywords.
    """
    matched_dataset=0
    text = customer_request.lower()
    # Tokenize the text by removing non-alphanumeric characters and splitting by whitespace
    tokens = re.findall(r'\b\w+\b', text)
    customer_tokens= set(tokens)

    for dataset, keywords in dataset_keywords.items():
        for keyword in keywords:
            if keyword in customer_tokens:
                matched_dataset= dataset


    if matched_dataset !=0:
        match matched_dataset:
            case "sale":

                df = pd.read_csv("datas/sales_yearly.csv")
                year=re.findall(r'\b20[0-9]{2}\b', text)[0]
                info= df[(df["Year"]==int(year))]

                return info

            case "customer":
                # df = pd.read_csv("datas/product_segment_analysis_sorted.csv")
                # filtered=filtered_data(df)
                # return filtered
                pass

            case "robot language":
                return generate_random_string(random()*100)

            
    else: 
        return "sorry, I'm stupid, haven't learned how to chat with human. Please follow the intruction or you can try to talk to me in my language, e.g. $%@^%$%^&*&^)"

