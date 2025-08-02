import ipywidgets as widgets
from IPython.display import display, clear_output
import math

# Heading
title = widgets.HTML("<h2 style='color:#2C3E50;'>Leap Year Checker 🗓️</h2>")

# Input widget
Year_base = widgets.BoundedFloatText(
    description="Year:",
    value=2024,
    min=0,
    max=9999,
    step=1,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='250px')
)

# Output widget
output = widgets.Output(layout={'border': '1px solid gray', 'padding': '10px', 'margin': '10px 0'})

# Button
calc_button = widgets.Button(
    description="Check Leap Year",
    button_style='success',
    icon='check',
    layout=widgets.Layout(width='250px')
)

# Clear button
clear_button = widgets.Button(
    description="Clear Output",
    button_style='warning',
    icon='trash',
    layout=widgets.Layout(width='250px')
)

# Function to calculate leap year
def calculate(b):
    with output:
        clear_output()
        try:
            year = int(Year_base.value)
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"✅ {year} is a Leap Year!")
            else:
                print(f"❌ {year} is NOT a Leap Year.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

# Clear function
def clear_output_area(b):
    with output:
        clear_output()

# Button clicks
calc_button.on_click(calculate)
clear_button.on_click(clear_output_area)

# Layout
buttons = widgets.VBox([calc_button, clear_button], layout=widgets.Layout(align_items='center'))
ui = widgets.VBox([title, Year_base, buttons, output])

display(ui)
