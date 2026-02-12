import tkinter as tk

def show_selection():
    selected_option = choice.get()
    result_label.config(text="You selected: " + selected_option)

# Create main window
root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x250")

# Variable to store selected value
choice = tk.StringVar()
choice.set("None")  # Default value

# Create radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=choice, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=choice, value="Option 2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=choice, value="Option 3")



# Button to show selected option
submit_button = tk.Button(root, text="Submit", command=show_selection)
submit_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
