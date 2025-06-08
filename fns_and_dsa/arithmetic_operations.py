<<<<<<< HEAD
# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the operation string.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: Result of the operation, or an error message for invalid operations or division by zero.
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
=======
def perform_operation(num1, num2, operation):
    """
    Performs the given arithmetic operation on two numbers.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): Operation to perform: 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float or str: Result of the operation or an error message
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
>>>>>>> 4250a18 (Implement perform_operation with basic arithmetic and error handling)
            if num2 == 0:
                return "Error: Cannot divide by zero."
            return num1 / num2
        case _:
<<<<<<< HEAD
            return "Error: Unsupported operation."
=======
            return "Error: Invalid operation."
>>>>>>> 4250a18 (Implement perform_operation with basic arithmetic and error handling)
