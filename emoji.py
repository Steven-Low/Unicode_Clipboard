import tkinter as tk
import math
from tkinter import *
import pyperclip

# Unicode symbols [arbitrarily append more...]
symbols = ["\u03C0", "\u03B1", "\u03B2", "\u03B3",
           "\u03B5", "\u2282", "\u2208", "\u2264",
           "\u222B", "\u03BE", "\u2211"]

def copy_to_clipboard(symbol):
    pyperclip.copy(symbol)

def create_button(root, symbol):
    button = tk.Button(root, text=symbol, width=10, height=5, font=('Arial', 16), command=lambda: copy_to_clipboard(symbol))
    #button.grid(sticky="nsew")
    return button

def create_gui():
    root = tk.Tk()
    root.title("Unicode Symbol Table")

    # Determine the window's least width & height
    width = math.ceil(math.sqrt(len(symbols))) # max cols
    height = math.ceil(len(symbols)/width)
    
    # Create a table of buttons
    for row in range(height):
        for col in range(width):
            if row * width + col >= len(symbols):
                symbol = "\u00D8"
            else:
                symbol = symbols[row * width + col]
            button = create_button(root, symbol)
            button.grid(row=row,column=col,sticky=SE)
    
    # Configure grid weights to make buttons expandable
    for i in range(width):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    
    root.mainloop()

# Run the GUI
create_gui()
