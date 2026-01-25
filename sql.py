from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
from google import genai

# Configure the new Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

## Function to load gemini model
def get_gemini_response(question, prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=[prompt[0], question]
    )
    return response.text

## Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"An error occurred with the SQL query: {e}")
        return []

## Define your prompt
prompt = [
    """
    You are an expert in converting English text into SQL queries!
    The SQL database has the name STUDENT and has the following columns: NAME, CLASS, SECTION.

    For example:
    Example 1: How many students are studying in Data Science class? 
    The SQL command will be: SELECT COUNT(*) FROM STUDENT WHERE CLASS="Data Science";

    Example 2: Tell me all the students studying in Data Science class? 
    The SQL command will be: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    
    also the sql code should not have ``` in the beginning or end of the output and no word 'sql' in the output.
    """
]

## Streamlit app
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print("first" ,response)
    response = read_sql_query(response, "student.db")
    print("second", response)
    st.subheader("The response is")
    for row in response:
        print(row)
        st.dataframe(row)