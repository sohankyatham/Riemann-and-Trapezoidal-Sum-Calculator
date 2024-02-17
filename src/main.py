# Riemann & Trapezoidal Sum Calculator with Python
# By Sohan Kyatham 

# This program estimates the area under a curve using numerical integration methods such as Riemann Sums (LRAM & RRAM) or the Trapezoidal Rule 

# Imports
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import webbrowser


# Create a tkinter window 
root = tk.Tk()
root.title("Riemann & Trapezoidal Sum Calculator with Python")
root.geometry("400x400")


# Function to plot the graph of f(x) and draws the shapes (representing sum approximation) to visual the integral
def plot_sum_approximation(total_sum, x_values, fx_values, approximation_type):
    # Plot the function f(x)
    plt.plot(x_values, fx_values, label='f(x)')
    # Label the x-axis and y-axis
    plt.xlabel('x')
    plt.ylabel('f(x)')
    # Title for the graph
    plt.title('Graph of f(x)')

    # Plot rectangles or trapezoids based on the selected approximation type
    if approximation_type == "left_riemann":
        # Iterate over the x_values to create left Riemann sum rectangles
        for i in range(len(x_values) - 1):
            # Fill the area under the function curve with rectangles
            plt.fill_between([x_values[i], x_values[i+1]], [fx_values[i], fx_values[i]], alpha=0.3)
    elif approximation_type == "right_riemann":
        # Iterate over the x_values to create right Riemann sum rectangles
        for i in range(1, len(x_values)):
            # Fill the area above the function curve with rectangles
            plt.fill_between([x_values[i-1], x_values[i]], [fx_values[i], fx_values[i]], alpha=0.3)
    elif approximation_type == "trapezoidal_sum":
        # Iterate over the x_values to create trapezoidal sum trapezoids
        for i in range(len(x_values) - 1):
            # Fill the area under the function curve with trapezoids
            plt.fill_between([x_values[i], x_values[i+1]], [fx_values[i], fx_values[i+1]], alpha=0.3)

    # Display the legend and show the plot
    plt.legend()
    plt.show()


# Performs the calculation using the desired approximation type
def calculate_sum(x_values, fx_values):
    # Set the total_sum to 0, allows repeated sum calculations
    total_sum = 0

    # Get the approximation_type from the radio button that the user selected
    approximation_type = radio_var.get()

    # Left Riemann Sum
    if approximation_type == "left_riemann":
        for i in range(len(x_values) - 1):
            # Get the width/base value of rectangle, represents the width of each sub interval (delta x)
            width = (x_values[i + 1] - x_values[i])
            # Get the height of the left-most point of the rectangle
            height = fx_values[i]
            # Calculate the total sum of the areas of every rectangle
            total_sum += (width * height)

    # Right Riemann Sum
    elif approximation_type == "right_riemann":
        for i in range(len(x_values) - 1):
            # Get the width/base value of rectangle, represents the width of each sub interval (delta x)
            base = (x_values[i + 1] - x_values[i])
            # Get the height of the right-most point of the rectangle
            height = fx_values[i + 1]
            # Calculate the total sum of the areas of every rectangle
            total_sum += (base * height)

    # Trapezoidal Sum
    elif approximation_type == "trapezoidal_sum":
        # Area of trapezoid is 0.5 * (base1 + base2) * height
        for i in range(len(x_values) - 1):
            # Get the height of the trapezoid, this is the different of the width of each sub interval (delta x)
            height = (x_values[i + 1] - x_values[i])
            # Get the first and second base values of the trapezoid
            base_1 = fx_values[i] 
            base_2 = fx_values[i + 1] 
            # Calculate the total sum of the areas of every trapezoid
            total_sum += 0.5 * (base_1 + base_2) * height
    
    # Update the total_sum_label to display the sum of the area 
    total_sum_label.config(text="Sum of Area: " + str(total_sum))

    # Call the plot_sum_approximation to graph the points and then graph the shapes under the curve depicting area
    plot_sum_approximation(total_sum, x_values, fx_values, approximation_type)


# Initializes/prepares the calculation by extracting x and f(x) values from user input
def initialize_calculation():
    global x_values
    global fx_values

    # Exception Handling to make sure that the user only enters numerical values as well as making sure x and f(x) have same number of values
    try:
        # x_values List Comprehension - Gets x values from entry and stores in array as individual numbers
        x_values = [float(x) for x in x_values_entry.get().split()]
        # fx_values List Comprehension - Gets f(x) values from entry and stores in array as individual numbers
        fx_values = [float(x) for x in fx_values_entry.get().split()]

        # Check if the user enters the same number of values for x and f(x)
        if len(x_values) == len(fx_values):
                # Call the calculate_sum function to perform the calculation using the desired approximation type
                calculate_sum(x_values, fx_values)
        else:
            # Display error message if the number of x and f(x) values are different
            messagebox.showerror("Error", "Th number of x and f(x) values must be equal")

    except ValueError:
        # Display error if the values of x and/or f(x) are not numerical
        messagebox.showerror("Error", "Values of x and f(x) must be numerical")


# Label for Entering x-values
x_value_label = tk.Label(root, text="Enter values of x:", font=("Arial", 11),)
x_value_label.pack(pady=5)
 
# Entry for Entering x-values
x_values_entry = tk.Entry(root, width=50)
x_values_entry.pack(pady=5)

# Label for Entering f(x) values
fx_value_label = tk.Label(root, text="Enter values for f(x):", font=("Arial", 11))
fx_value_label.pack(pady=5)

# Entry for Entering f(x) values
fx_values_entry = tk.Entry(root, width=50)
fx_values_entry.pack(pady=5)


# Frame for Storing Radio Buttons
radio_btns_frame = tk.Frame(root)
radio_btns_frame.pack(pady=10)

# Label for Selecting Approximation Type
approximation_type_label = tk.Label(radio_btns_frame, text="Select Approximation Type:", font=("Arial", 11))
approximation_type_label.pack()

# radio_var for helping select the radio buttons and getting the value
radio_var = tk.StringVar(value="left_riemann")
# Radio Button for Left Riemann Sum
left_riemann_radio = tk.Radiobutton(radio_btns_frame, text="Left Riemann Sum (LRAM)", variable=radio_var, value="left_riemann")
left_riemann_radio.pack(anchor=tk.W)

# Radio Button for Right Riemann Sum
right_riemann_radio = tk.Radiobutton(radio_btns_frame, text="Right Riemann Sum (RRAM)", variable=radio_var, value="right_riemann")
right_riemann_radio.pack(anchor=tk.W)

# Radio Button for Trapezoidal Sum
trapezoidal_sum_radio = tk.Radiobutton(radio_btns_frame, text="Trapezoidal Sum", variable=radio_var, value="trapezoidal_sum")
trapezoidal_sum_radio.pack(anchor=tk.W)


# Calculate Button
calculate_btn = tk.Button(root, text="Calculate", width=16, font=("Arial", 11), bg="#26aceb", command=initialize_calculation)
calculate_btn.pack(pady=10)

# Total Sum Label
total_sum_label = tk.Label(root, text="Sum of Area: ...", font=("Arial", 11))
total_sum_label.pack(pady=15)

# menu_bar - Place for Placing Menu Options
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# file_menu - Graph options for clearing & saving graph + exiting program
file_menu = tk.Menu(menu_bar, tearoff=False)
# Add the graph_menu to the menu_bar
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Graph as Image", accelerator="Ctrl+s")
file_menu.add_separator()
file_menu.add_command(label="Exit Window", accelerator="Alt-F4")

# help_menu - About & Documentation
help_menu = tk.Menu(menu_bar, tearoff=False)
# Add the about_menu to the menu_bar
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="View Project Repository")#, command=view_project)
help_menu.add_command(label="About")#, command=about_screen)

# Mainloop
root.mainloop()