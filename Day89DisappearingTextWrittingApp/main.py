import tkinter as tk
from tkinter import messagebox


class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed App")
        self.root.geometry("400x300")

        # Initialize variables
        self.last_keypress_time = None
        self.delay_time = 5000  # 5 seconds delay in milliseconds
        self.typing_active = False

        # Create text widget
        self.text_widget = tk.Text(self.root, height=10, width=50)
        self.text_widget.pack(pady=20)

        # Create label for instructions
        self.label = tk.Label(self.root, text="Type something! If you stop for 5 seconds, your text will be cleared.")
        self.label.pack(pady=10)

        # Bind key press event to detect typing
        self.text_widget.bind("<KeyPress>", self.on_key_press)

        # Start checking for inactivity
        self.check_inactivity()

    def on_key_press(self, event):
        """Callback function when any key is pressed."""
        self.typing_active = True  # Typing is detected

        # Cancel the previous after event if one exists
        if self.last_keypress_time is not None:
            self.root.after_cancel(self.last_keypress_time)

        # Start a new after event to clear the text after the delay
        self.last_keypress_time = self.root.after(self.delay_time, self.clear_text)

    def clear_text(self):
        """Clear text if no key has been pressed for 5 seconds."""
        self.typing_active = False
        self.text_widget.delete("1.0", tk.END)
        messagebox.showinfo("Alert", "Text cleared due to inactivity!")

    def check_inactivity(self):
        """Keep checking every second for inactivity."""
        # We can remove this check since after-cancel is already handled
        self.root.after(1000, self.check_inactivity)  # Keep checking every second


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
