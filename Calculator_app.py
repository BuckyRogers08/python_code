import ipywidgets as widgets
from IPython.display import display, clear_output
import math

# Input widgets
num1 = widgets.FloatText(description="Num 1:", value=0)
num2 = widgets.FloatText(description="Num 2:", value=0)

# Dropdown for operation
operation = widgets.Dropdown(
    options=["+", "-", "*", "/", "sqrt", "log", "sin", "cos", "tan", "%", "^"],
    value="+",
    description="Op:"
)

# Output widget
output = widgets.Output()

# Button to trigger calculation
calc_button = widgets.Button(description="Calculate", button_style='success')

# Calculation logic
def calculate(b):
    with output:
        clear_output()
        try:
            n1 = num1.value
            n2 = num2.value
            op = operation.value
            
            if op == "+":
                result = n1 + n2
            elif op == "-":
                result = n1 - n2
            elif op == "*":
                result = n1 * n2
            elif op == "/":
                if n2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = round(n1 / n2, 3)
            elif op == "sqrt":
                result = round(math.sqrt(n1), 3)
            elif op == "log":
                result = round(math.log(n1), 3)
            elif op == "sin":
                result = round(math.sin(math.radians(n1)), 3)
            elif op == "cos":
                result = round(math.cos(math.radians(n1)), 3)
            elif op == "tan":
                result = round(math.tan(math.radians(n1)), 3)
            elif op == "%":
                result = n1 % n2
            elif op == "^":
                result = n1 ** n2
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

# Link button to function
calc_button.on_click(calculate)

# Display all widgets
display(num1, num2, operation, calc_button, output)
