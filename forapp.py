import streamlit as st
import time

# Simple Calculator in Streamlit

st.title("Simple Calculator")

# Function for calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Add a small delay to simulate loading
def simulate_delay():
    with st.spinner("Calculating..."):
        time.sleep(2)  # 2-second delay

# User inputs
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Perform operation based on user input
if st.button("Calculate"):
    simulate_delay()  # Simulate loading delay

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
