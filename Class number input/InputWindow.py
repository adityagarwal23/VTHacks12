import tkinter as tk
from tkinter import messagebox

def submit_action():
    # Get the values from the text boxes
    text_box1_value = text_box1.get()
    text_box2_value = text_box2.get()
    
    # Prepare content for the text file
    content = f"Text Box 1: {text_box1_value}\nText Box 2: {text_box2_value}\n"
    
    # Write content to a text file, overwriting the existing content
    try:
        with open('output.txt', 'w') as file:
            file.write(content)
        messagebox.showinfo("Success", "Data saved to output.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write to file: {e}")

# Create the main window
root = tk.Tk()
root.title("Text Box Entries")

# Create and place the first text box
tk.Label(root, text="Text Box 1:").grid(row=0, column=0, padx=10, pady=10)
text_box1 = tk.Entry(root)
text_box1.grid(row=0, column=1, padx=10, pady=10)

# Create and place the second text box
tk.Label(root, text="Text Box 2:").grid(row=1, column=0, padx=10, pady=10)
text_box2 = tk.Entry(root)
text_box2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
