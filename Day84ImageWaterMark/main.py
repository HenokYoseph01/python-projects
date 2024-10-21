import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")
        self.root.geometry("800x600")

        self.image_path = None
        self.watermark_text = None
        self.watermark_image = None
        self.loaded_image = None

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Label: Title
        self.title_label = tk.Label(self.root, text="Watermark Application", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Button: Upload Image
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image, font=("Arial", 14))
        self.upload_button.pack(pady=10)

        # Image Canvas
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg='gray')
        self.canvas.pack(pady=10)

        # Text Entry: Watermark Text
        self.watermark_entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.watermark_entry.pack(pady=5)
        self.watermark_entry.insert(0, "Enter Watermark Text Here...")

        # Button: Apply Watermark (Text)
        self.apply_text_button = tk.Button(self.root, text="Apply Watermark Text", command=self.apply_text_watermark, font=("Arial", 14))
        self.apply_text_button.pack(pady=10)

        # Button: Upload Watermark Logo (Optional)
        self.upload_logo_button = tk.Button(self.root, text="Upload Watermark Logo", command=self.upload_watermark_logo, font=("Arial", 14))
        self.upload_logo_button.pack(pady=5)

        # Button: Save Image
        self.save_button = tk.Button(self.root, text="Save Watermarked Image", command=self.save_image, font=("Arial", 14))
        self.save_button.pack(pady=20)

    def upload_image(self):
        """Function to upload the main image."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(self.image_path)
            img.thumbnail((500, 400))
            self.loaded_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(250, 200, image=self.loaded_image)
            messagebox.showinfo("Image Uploaded", "Image uploaded successfully!")

    def apply_text_watermark(self):
        """Function to apply text watermark on the image."""
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        watermark_text = self.watermark_entry.get()
        if not watermark_text:
            messagebox.showerror("Error", "Please enter watermark text!")
            return

        # Open the image
        image = Image.open(self.image_path)
        watermark_image = image.copy()

        # Create ImageDraw object
        draw = ImageDraw.Draw(watermark_image)

        # Set font
        font = ImageFont.truetype("arial.ttf", 50)

        # Add text to the image (Bottom-Right corner)
        width, height = image.size
        text_width, text_height = draw.textsize(watermark_text, font=font)
        text_position = (width - text_width - 10, height - text_height - 10)
        draw.text(text_position, watermark_text, font=font, fill=(255, 255, 255, 128))  # White with transparency

        # Save watermarked image to a temporary variable
        self.watermark_image = watermark_image

        # Show the watermarked image on the canvas
        watermark_image.thumbnail((500, 400))
        self.loaded_image = ImageTk.PhotoImage(watermark_image)
        self.canvas.create_image(250, 200, image=self.loaded_image)

        messagebox.showinfo("Success", "Watermark text added successfully!")

    def upload_watermark_logo(self):
        """Function to upload a watermark logo and apply it."""
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if logo_path:
            # Open the main image and the logo image
            image = Image.open(self.image_path)
            logo = Image.open(logo_path)

            # Resize the logo
            logo.thumbnail((100, 100))

            # Add logo to the bottom-right corner
            width, height = image.size
            logo_width, logo_height = logo.size
            position = (width - logo_width - 10, height - logo_height - 10)
            image.paste(logo, position, logo)

            # Save the watermarked image
            self.watermark_image = image

            # Show the watermarked image on the canvas
            image.thumbnail((500, 400))
            self.loaded_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(250, 200, image=self.loaded_image)

            messagebox.showinfo("Success", "Watermark logo added successfully!")

    def save_image(self):
        """Function to save the watermarked image."""
        if self.watermark_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.watermark_image.save(save_path)
                messagebox.showinfo("Image Saved", f"Watermarked image saved to {save_path}")
        else:
            messagebox.showerror("Error", "No watermarked image to save!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
