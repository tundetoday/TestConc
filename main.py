import tkinter as tk

# Function to change the label text
def change_label_text():
    label.config(text="Hello, Tkinter!")

# Create the main application window
app = tk.Tk()
app.title("Basic Tkinter App")
app.geometry("300x200")  # Set the size of the window

# Create a label widget
label = tk.Label(app, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add some vertical padding

# Create a button widget
button = tk.Button(app, text="Click Me!", command=change_label_text)
button.pack(pady=10)  # Add some vertical padding

# Start the Tkinter event loop
app.mainloop()