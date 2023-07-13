# Unicode_Clipboard

This Python code creates a graphical user interface (GUI) using Tkinter to display a table of Unicode symbols. When a symbol button is clicked, it will be copied to the clipboard.

## Prerequisites

- Python 3.x
- Tkinter library
- Pyperclip library

## Installation

1. Clone the repository
2. Change to the repository directory
3. Install the required libraries using pip

## Description

The code uses the Tkinter library to create the GUI. It imports necessary libraries and defines functions for copying symbols to the clipboard.
The Unicode symbols are stored in a list, and the code dynamically determines the table dimensions based on the number of symbols. Buttons are created for each symbol and placed in a grid layout.
The grid weights are configured to allow buttons to expand. Clicking a button copies the corresponding symbol to the clipboard using the Pyperclip library.

## Customization

- To add more Unicode symbols, simply append them to the `symbols` list in the code.
- You can modify the font, button dimensions, or any other GUI properties to suit your preferences.

Feel free to customize and extend the code according to your needs!

## Demo
<img width="273" alt="image" src="https://github.com/Steven-Low/Unicode_Clipboard/assets/106484271/22fbdf66-ac5c-464b-8a3f-4a5cafa808b4">
