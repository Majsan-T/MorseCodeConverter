import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage, Canvas

# Dictionary for Morse Code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    'Å': '.--.-', 'Ä': '.-.-', 'Ö': '---.', 'Ü': '..--', 'Ñ': '--.--'
}

# Function to convert text to Morse Code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '/ '  # Separator for spaces between words
    return morse_code.strip()


# Function to convert Morse Code to text
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse.split(' / ')  # Split by words
    decoded_text = ''
    for word in words:
        for char in word.split():
            decoded_text += reverse_dict.get(char, '')
        decoded_text += ' '  # Add space between words
    return decoded_text.strip()

# Function to handle Text to Morse Code conversion
def handle_text_to_morse():
    user_input = text_entry.get()
    if user_input.strip():
        global result
        result = text_to_morse(user_input)
        result_label.config(text=f"Morse Code: {result}")
        back_button.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Error", "Please enter text to convert!")

# Function to handle Morse Code to Text conversion
def handle_morse_to_text():
    user_input = text_entry.get()
    if user_input.strip():
        global result
        result = morse_to_text(user_input)
        result_label.config(text=f"Text: {result}")
        back_button.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Error", "Please enter Morse Code to convert!")

# Function to translate back
def handle_translate_back():
    if result:
        if all(c in ".-/ " for c in result):  # Check if the result is Morse Code
            back_result = morse_to_text(result)
            result_label.config(text=f"Back to Text: {back_result}")
        else:
            back_result = text_to_morse(result)
            result_label.config(text=f"Back to Morse Code: {back_result}")
    else:
        messagebox.showerror("Error", "No result to translate back!")

# Function to exit the program
def exit_program():
    window.destroy()

# Main window
window = tk.Tk()
window.title("Text and Morse Code Converter")
window.geometry("550x300")

# Background Image
bg_img = PhotoImage(file="bg-img.png")  # Make sure this file is accessible
background_label = tk.Label(window, image=bg_img)
background_label.place(relwidth=1, relheight=1)

# Configure grid columns
window.grid_columnconfigure(0, weight=1)  # Outer column (left)
window.grid_columnconfigure(1, weight=2)  # Center column
window.grid_columnconfigure(2, weight=1)  # Outer column (right)

# Instruction Label
instruction_label = tk.Label(window, bg="#c2cece", text="Enter Text or Morse Code:", font=("Arial", 16, "bold"))
instruction_label.grid(row=0, column=1, pady=10)

# Text Entry
text_entry = tk.Entry(window, width=50)
text_entry.grid(row=1, column=1, pady=10)

# Buttons with adjusted width and font
text_to_morse_button = tk.Button(window, text="Text to Morse Code", command=handle_text_to_morse, width=25, font=("Arial", 10))
text_to_morse_button.grid(row=2, column=0, padx=10, pady=20, sticky="ew")

back_button = tk.Button(window, text="Translate Back", command=handle_translate_back, state=tk.DISABLED)
back_button.grid(row=2, column=1, pady=20)

morse_to_text_button = tk.Button(window, text="Morse Code to Text", command=handle_morse_to_text, width=25, font=("Arial", 10))
morse_to_text_button.grid(row=2, column=2, padx=10, pady=20, sticky="ew")

# Result Label
result_label = tk.Label(window, text="Result", font=("Arial", 12), bg="#FFFFFF", width=50)
result_label.grid(row=3, column=1, pady=10)

# Exit Button
exit_button = tk.Button(window, text="EXIT", command=exit_program)
exit_button.grid(row=4, column=2, padx=20, pady=30, sticky="e")

# Run the Tkinter event loop
window.mainloop()
