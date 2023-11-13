import random


def generate_arbitrary_integer(min_value, max_value):
    """
    Generates a arbitrary integer within the specified range.

    Parameters:
    - min_value (int): Minimum value of the range.
    - max_value (int): Maximum value of the range.

    Returns:
    - int or None: Random integer within the specified range, or None if an error occurs.
    """
    try:
        # Check if both min_value and max_value are integers
        if not isinstance(min_value, int) or not isinstance(max_value, int):
            raise ValueError("Both min and max should be integers.")
        
        # Check if min_value is less than or equal to max_value
        if min_value > max_value:
            raise ValueError("min should be less than or equal to max.")

        # Generate and return an arbitrary integer
        return random.randint(min_value, max_value)
    
    except ValueError as e:
        # Handle the error and print a meaningful message
        print(f"Error: {e}")
        return None


def choose_arbitrary_operator():
    """
    Returns an arbitrary chosen mathematical operator from the list ['+', '-', '*'].

    Returns:
    - str: Arbitrary chosen operator.
    """
    try:
        # Return an arbitrary operator from the list
        return random.choice(['+', '-', '*'])
    
    except IndexError:
        # Handle the error if the list is empty
        print("Error: The list of operators is empty.")
        return None

# Example usage:
selected_operator = choose_arbitrary_operator()
print(f"Selected Operator: {selected_operator}")
    

def perform_operation(number1, number2, operator):
    """
    Performs a mathematical operation on two numbers.

    Parameters:
    - number1 (float): The first number.
    - number2 (float): The second number.
    - operator (str): Mathematical operator ('+', '-', '*').

    Returns:
    - tuple or None: A tuple with a string representation of the operation and the result,
                    or None if an error occurs.
    """
    try:
        # Perform the operation based on the operator
        if operator in {'+', '-', '*'}:
            result = eval(f"{number1} {operator} {number2}")
        else:
            raise ValueError("Invalid operator. Supported operators are '+', '-', '*'.")

        # Return a tuple with the operation string and the result
        return f"{number1} {operator} {number2}", result

    except Exception as e:
        # Handle any unexpected errors and print a meaningful message
        print(f"Error: {e}")
        return None


def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
