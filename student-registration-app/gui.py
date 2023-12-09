import sys
import tkinter as tk
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from csv_maker import MakeIt




def validate_input(char):
    # This function is called for each character the user types
    # It returns True if the input is valid (an integer), and False otherwise
    return char.isdigit() or char == ""

def on_button_click():
    studentId = studentIdEntry.get()
    studentName = studentNameEntry.get()
    if not studentId or not studentName:
        notifierLabel.config(text="Entering value of student Id and name is must")
    else:
        studentId = int(studentId)
        maker = MakeIt()
        str = maker.makeCSV(studentId, studentName)
        notifierLabel.config(text=str)



# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry(f"{400}x{500}")
# root.pack(anchor = 'nw')

frame = tk.Frame(root, width=400, height=500)
frame.pack(anchor='nw', padx=20, pady= 20)

validation = frame.register(validate_input)

# Student Id Label and Entry using grid
studentIdLabel = tk.Label(frame, text="Student Id")
studentIdLabel.grid(row=0, column=0, pady=10, sticky=tk.W)

studentIdEntry = tk.Entry(frame, width=20, validate="key", validatecommand=(validation, "%S"))
studentIdEntry.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

# Text Entry, Button, and Label using grid
studentNameLabel = tk.Label(frame, text="Student Name")
studentNameLabel.grid(row=1, column=0, pady=10, sticky=tk.W)

studentNameEntry = tk.Entry(frame, width=20)
studentNameEntry.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)


button = tk.Button(frame, text="Click Me", command=on_button_click)
button.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

notifierLabel = tk.Label(frame, text="")
notifierLabel.grid(row=3, column=0, pady=10, sticky=tk.W)



# Run the Tkinter event loop
root.mainloop()