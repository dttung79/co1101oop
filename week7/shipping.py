from tkinter import *

# Dictionary containing the shipping methods and their corresponding costs
shipping_methods = {
    'Standard': 5.0,
    'Express': 10.0,
    'Priority': 15.0
}

def calculate_shipping():
    # Retrieve the selected shipping method and the values from the respective widgets
    selected_method = var_shipping.get()
    weight = float(txt_weight.get())
    distance = float(txt_distance.get())
    
    # Adjust weight based on the selected unit
    if var_weight_unit.get() == 'Pounds':
        weight *= 0.45359237  # Convert pounds to kilograms
    
    # Adjust distance based on the selected unit
    if var_distance_unit.get() == 'Miles':
        distance *= 1.609344
    
    # Calculate the total shipping cost based on weight, distance, and the shipping method cost
    total_cost = (weight * 0.1) + (distance * 0.05) + shipping_methods[selected_method]
    
    # Update the total cost label with the calculated value
    lbl_total_cost.config(text=f"Total cost: ${total_cost:.2f}")

# Create the main window
window = Tk()
window.title("Shipping Cost Calculator")

# Create a label for the shipping method selection
lbl_method = Label(window, text="Select a shipping method:")
lbl_method.grid(row=0, column=0, sticky=W)

# Create a variable to hold the selected shipping method
var_shipping = StringVar(window)
var_shipping.set('Standard')  # Set a default shipping method

# Create an OptionMenu for shipping method selection
cb_shipping = OptionMenu(window, var_shipping, *shipping_methods.keys(), \
                         command=calculate_shipping)
cb_shipping.grid(row=0, column=1, sticky=W)

# Create a label for the weight input
lbl_weight = Label(window, text="Enter weight:")
lbl_weight.grid(row=1, column=0, sticky=W)

# Create an entry widget for the weight input
txt_weight = Entry(window)
txt_weight.grid(row=1, column=1, sticky=W)

# Create a variable to hold the selected weight unit
var_weight_unit = StringVar(window)
var_weight_unit.set('Kilograms')  # Set a default weight unit

# Create radio buttons for weight unit selection
lbl_weight_unit = Label(window, text="Weight unit:")
lbl_weight_unit.grid(row=2, column=0, sticky=W)

rd_kilograms = Radiobutton(window, text="Kilograms", variable=var_weight_unit, value='Kilograms')
rd_kilograms.grid(row=2, column=1, sticky=W)

rd_pounds = Radiobutton(window, text="Pounds", variable=var_weight_unit, value='Pounds')
rd_pounds.grid(row=2, column=2, sticky=W)

# Create a label for the distance input
lbl_distance = Label(window, text="Enter distance:")
lbl_distance.grid(row=3, column=0, sticky=W)

# Create an entry widget for the distance input
txt_distance = Entry(window)
txt_distance.grid(row=3, column=1, sticky=W)

# Create a variable to hold the selected distance unit
var_distance_unit = StringVar(window)
var_distance_unit.set('Kilometers')  # Set a default distance unit

# Create radio buttons for distance unit selection
lbl_distance_unit = Label(window, text="Distance unit:")
lbl_distance_unit.grid(row=4, column=0, sticky=W)

rd_kilometers = Radiobutton(window, text="Kilometers", variable=var_distance_unit, \
                            value='Kilometers')
rd_kilometers.grid(row=4, column=1, sticky=W)

rd_miles = Radiobutton(window, text="Miles", variable=var_distance_unit, value='Miles')
rd_miles.grid(row=4, column=2, sticky=W)

# Create a button to calculate the total shipping cost
btn_calculate = Button(window, text="Calculate", command=calculate_shipping)
btn_calculate.grid(row=5, column=1, sticky=W)

# Create a label to display the total shipping cost
lbl_total_cost = Label(window, text="Total Shipping cost: $")
lbl_total_cost.grid(row=6, column=0, columnspan=3)

# Start the Tkinter event loop
window.mainloop()
