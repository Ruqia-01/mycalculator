from Addition import sum
from Subtraction import subtract
from Multiplication import multiply
from Division import divide
def main():
    try:
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        operator = input("Enter operator(+,-,*,/):")

        if operator == "+":
            solution = sum(a, b)
        elif operator == "-":
            solution = subtract(a, b)
        elif operator == "*":
            solution = multiply(a, b)
        elif operator == "/":
            solution = divide(a, b)
        else:
            print("Invalid operator.Please enter one of +,-,*,/. ")

            main()
            if operator is invalid:
                return
        print(f"solution is: {solution}")

    except ValueError:
        print("Invalid input.Please enter numeric value.")
        main()
        if input is invalid:
            return

    except NameError:
        print("NameError: Name is not defined.")

    except Exception as e:
        print(f"An error occured: {e}.")

    quit = input("Do you want to quit ? (Y/N):")

    if quit == "N":
        main()

    elif quit == "Y":
        print("Thanks!")

    else:
        print("invalid input.")
        quit

main()