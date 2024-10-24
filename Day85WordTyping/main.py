import tkinter as tk
import time
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

# Sample text for users to type
sample_text = "The quick brown fox jumps over the lazy dog."

# Global variables for tracking time
start_time = 0
end_time = 0

# Create a label for the instructions
instruction_label = tk.Label(root, text="Type the following text as fast as you can:")
instruction_label.pack(pady=10)

# Create a label to display the sample text
sample_label = tk.Label(root, text=sample_text, font=("Arial", 14))
sample_label.pack(pady=10)

# Create a text entry widget for the user to type in
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=10)

# Create labels for showing the typing speed result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)


# Function to start the test
def start_test():
    global start_time
    input_text.delete(1.0, tk.END)
    result_label.config(text="")
    start_time = time.time()


# Function to stop the test and calculate typing speed
def stop_test():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    entered_text = input_text.get(1.0, tk.END).strip()
    word_count = len(entered_text.split())
    wpm = word_count / (elapsed_time / 60)

    # Compare the entered text with the sample text for accuracy
    if entered_text == sample_text:
        result_label.config(text=f"Correct! You typed at {wpm:.2f} words per minute.")
    else:
        result_label.config(text=f"Your typing speed is {wpm:.2f} words per minute, but some words were incorrect.")


# Create Start and Stop buttons
start_button = tk.Button(root, text="Start", command=start_test)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_test)
stop_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
