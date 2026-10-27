import streamlit as st

st.title("\t\t\t Calculator")
st.write("Enter two numbers and choose an operation below:")

num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

operation = st.selectbox(
    "Select operation:",
    ("1) Add", "2) Subtract", "3) Multiply", "4) Division")
)

if st.button("Calculate"):
    if operation == "1) Add":
        result = num1 + num2
        st.success(f"Addition result: {result}")
        
    elif operation == "2) Subtract":
        result = num1 - num2
        st.success(f"Subtraction result: {result}")
        
    elif operation == "3) Multiply":
        result = num1 * num2
        st.success(f"Multiplication result: {result}")
        
    elif operation == "4) Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Division result: {result}")
        else:
            st.error("Error! Division by zero is not allowed.")