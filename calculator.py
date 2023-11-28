# Calculator.py
# Example Simple Python Flask Calculator Application Web

"""
Calculator functions for doing math operations on numbers.
"""

# Dependencies - Flask, render_template, request, math
import math
from flask import Flask, render_template, request


# Initialize the Flask application
app = Flask(__name__, template_folder="templates")


# Routes of the application flask
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Function index to run the calculator

    Args:
        number1 (float): First number
        number2 (float): Second number
        operation (int): Operation to do

    Returns:
        result (string): Result of the operation/exception
    """
    # Initialize the result to None
    result = None
    # Initialize the operation to 1 (add)
    operation = 1
    # Check if the request method is POST
    if request.method == "POST":
        try:
            # Get the values from the form
            number1 = float(request.form["number1"])
            number2 = float(request.form["number2"])
            operation = int(request.form["operation"])
            # If the operation is add
            if operation == 1:
                # Do the operation
                result = add(number1, number2)
            # If the operation is subtract
            elif operation == 2:
                # Do the operation
                result = subtract(number1, number2)
            # If the operation is multiply
            elif operation == 3:
                # Do the operation
                result = multiply(number1, number2)
            # If the operation is divide
            elif operation == 4:
                # Do the operation
                result = divide(number1, number2)
            # If the operation is pow
            elif operation == 5:
                # Do the operation
                result = mathpow(number1, number2)
        # If the values are not numbers, show the error
        except ValueError:
            # Show the error in the screen
            result = "* Sorry, enter numbers please *"
    # Render the template with the result
    return render_template("index.html", result=result)


def add(number1, number2):
    """
    Function to add two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Sum of number1 + number2
    """
    return number1 + number2


def subtract(number1, number2):
    """
    Function to substract two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Substract of number1 - number2
    """
    return number1 - number2


def multiply(number1, number2):
    """
    Function to multiply two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Multiply of number1 * number2
    """
    return number1 * number2


def divide(number1, number2):
    """
    Function to divide two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Divide of number1 / number2
    """
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Division by zero is not allowed !!!!!"


def mathpow(number1, number2):
    """
    Function to calculte the pow used two numbers, number1^number2

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Pow of number1^number2
    """
    return math.pow(number1, number2)


# Run the application
if __name__ == "__main__":
    app.run(debug=False)
