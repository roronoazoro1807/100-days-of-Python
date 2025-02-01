import tkinter as tk

# Function to convert miles to km
def convert():
    miles = float(miles_input.get())  # Get input from entry field
    km = miles * 1.60934  # Convert to kilometers
    result_label.config(text=f"{km:.2f}")  # Update result label

# Create main window
root = tk.Tk()
root.title("Miles to Km Converter")
root.config(padx=20, pady=20)

# Entry for miles input
miles_input = tk.Entry(root, width=10)
miles_input.grid(row=0, column=1)

# Labels
tk.Label(root, text="Miles").grid(row=0, column=2)
tk.Label(root, text="is equal to").grid(row=1, column=0)

result_label = tk.Label(root, text="0")  # Result placeholder
result_label.grid(row=1, column=1)

tk.Label(root, text="Km").grid(row=1, column=2)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1)

root.mainloop()
