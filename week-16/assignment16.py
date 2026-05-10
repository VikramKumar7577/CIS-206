import tkinter as tk
from tkinter import messagebox


# This function runs when the button is clicked.
# It checks the age, does the calculation and show the result.
def calculate_age():
    name = name_entry.get()
    age_text = age_entry.get()

    if name == "":
        messagebox.showerror("Error", "Please enter a name.")
        return

    if not age_text.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return

    age = int(age_text)
    next_year_age = age + 1

    result_label.config(
        text=f"Hello {name}. Next year you will be {next_year_age}."
    )


# Main window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("350x220")

# Name input
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

# Age input
age_label = tk.Label(window, text="Enter your age:")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()

# Button to run the calculation
calc_button = tk.Button(window, text="Calculate", command=calculate_age)
calc_button.pack(pady=10)

# Result output
result_label = tk.Label(window, text="")
result_label.pack()

# Keep the window open
window.mainloop()