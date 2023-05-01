import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st

# Initialize
cred = credentials.Certificate("integratekey.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://database-2d9f4-default-rtdb.firebaseio.com/'})
ref = db.reference('/employees')  
st.header("Add Employee")
emp_id = st.text_input("Employee_Id")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120)
salary = st.number_input("Salary", min_value=0)
if st.button("Submit"):
    employee_data = {
        "name": name,
        "age": age,
        "salary": salary
    }
    ref.child(emp_id).set(employee_data)
    st.success("Employee data added to Firebase!")
