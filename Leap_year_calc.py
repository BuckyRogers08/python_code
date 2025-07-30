import ipywidgets as widgets
from IPython.display import display, clear_output
import math

# Input widgets
Year_base = widgets.FloatText(description="Year", value=0)

# Output widget
output = widgets.Output()

# Button to trigger calculation
calc_button = widgets.Button(description="Calculate", button_style='success')

# Calculation logic
def calculate(b):
    with output:
        clear_output()
        try:
            Year = Year_base.value
            if Year%4==0 and Year%100!=0 or Year%400 == 0:
              print("leap year")
            else:
              print("not a leap year")

        except Exception as e:
            print(f"Error: {e}")

# Link button to function
calc_button.on_click(calculate)

# Display all widgets
display(Year_base, calc_button, output)


