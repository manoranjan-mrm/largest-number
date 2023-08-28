import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

st.title("Find the Largest Number")

# Input fields for three numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest Number"):
    if num1 == num2 == num3:
        st.error("All three numbers are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest}")