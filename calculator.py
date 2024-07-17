import streamlit as st
from Addition import sum
from Subtraction import subtract
from Multiplication import multiply
from Division import divide

def main():
    st.title("Simple Calculator")
    st.subheader("Perform Operations on Two Numbers")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")

    operation = st.selectbox("Select operation:", ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"))

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = sum(a, b)
                st.success(f"Result of {a} + {b} = {result}")

            elif operation == "Subtraction (-)":
                result = subtract(a, b)
                st.success(f"Result of {a} - {b} = {result}")

            elif operation == "Multiplication (*)":
                result = multiply(a, b)
                st.success(f"Result of {a} * {b} = {result}")

            elif operation == "Division (/)":
                if b == 0:
                    st.error("Cannot divide by zero.")
                else:
                    result = divide(a, b)
                    st.success(f"Result of {a} / {b} = {result}")

        except ValueError:
            st.error("Invalid input. Please enter numeric values.")
        

        except Exception as e:
            st.error(f"An error occured: {e}.")

    quit_choice = st.radio("Do you want to quit?", ("Yes", "No"))

    if quit_choice == "No":
        st.write("Choose new numbers and operation or quit.")
    else:
        st.write("Thanks for using the calculator!")

if __name__ == "__main__":
    main()
