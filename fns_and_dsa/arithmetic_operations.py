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
            if num2 == 0:
                return "Error: Cannot divide by zero."
            return num1 / num2
        case _:
            return "Error: Unsupported operation."
