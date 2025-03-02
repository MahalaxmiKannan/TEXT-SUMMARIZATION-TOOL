import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
import warnings
import os

# Suppress the TensorFlow deprecation warning (optional)
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')

# Initialize the summarization pipeline with a specific model (This will download once and cache it locally)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")  # Use PyTorch

def summarize_text():
    # Get the input text from the text area
    input_text = text_input.get("1.0", tk.END).strip()  # Get text from input box
    
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to summarize!")
        return
    
    try:
        # Summarize the text using the model
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
        
        # Display the summarized text in the output text area
        summary_text.delete("1.0", tk.END)  # Clear previous output
        summary_text.insert(tk.END, summary[0]['summary_text'])
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window for the Tkinter GUI
root = tk.Tk()
root.title("Text Summarization Tool")
root.geometry("800x600")  # Increased window size for larger text areas

# Create and place a label for instructions
label = tk.Label(root, text="Enter Text to Summarize:", font=("Arial", 16))  # Larger font size
label.pack(pady=15)

# Create a text box for user input (to enter the text to be summarized) with larger size and font
text_input = tk.Text(root, height=12, width=80, wrap=tk.WORD, font=("Arial", 12))  # Larger text area
text_input.pack(pady=15)

# Create a button to trigger the summarization process with larger text
summarize_button = tk.Button(root, text="Summarize Text", font=("Arial", 14), command=summarize_text)  # Larger button text
summarize_button.pack(pady=15)

# Create a text box for displaying the summarized text with larger size and font
summary_text = tk.Text(root, height=12, width=80, wrap=tk.WORD, font=("Arial", 12))  # Larger output area
summary_text.pack(pady=15)

# Run the Tkinter main loop (this displays the window)
root.mainloop()
