import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()

    if value == 'AC':
        entry_var.set('')
    elif value == 'delete':
        entry_var.set(current_text[:-1])
    elif value == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set('Error')
    elif value == '%':
        entry_var.set(str(eval(current_text) / 100))
    else:
        entry_var.set(current_text + value)

# Create the main window
root = tk.Tk()
root.title("CALCULATOR--2024")

# Entry widget for displaying the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Define the button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('AC', 5, 0), ('DEL', 5, 1), ('=', 5, 2), ('00', 5, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 12),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

# Run the main loop
root.mainloop()
