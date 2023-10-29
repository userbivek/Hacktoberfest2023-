import math

def main():
    print("Scientific Calculator")
    while True:
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'sqrt' for square root")
        print("Enter 'log' for logarithm")
        print("Enter 'exp' for exponentiation")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ["add", "sub", "mul", "div", "sqrt", "log", "exp"]:
            try:
                num1 = float(input("Enter first number: "))
                if user_input not in ["sqrt", "log", "exp"]:
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if user_input == "add":
                print("Result: ", num1 + num2)
            elif user_input == "sub":
                print("Result: ", num1 - num2)
            elif user_input == "mul":
                print("Result: ", num1 * num2)
            elif user_input == "div":
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print("Result: ", num1 / num2)
            elif user_input == "sqrt":
                print("Result: ", math.sqrt(num1))
            elif user_input == "log":
                if num1 <= 0 or num2 <= 0 or num2 == 1:
                    print("Invalid input for logarithm.")
                else:
                    print("Result: ", math.log(num1, num2))
            elif user_input == "exp":
                print("Result: ", math.pow(num1, num2))
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
