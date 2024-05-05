import tkinter as tk

def count_words():
    text = text_entry.get("1.0", "end-1c")
    word_count = len(text.split())
    result_label.config(text=f"Word Count: {word_count}")

# Creating the main window
root = tk.Tk()
root.title("Word Counter")

# creating Text entry widget
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=10)

# Button to trigger word count
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

# Label to display the word count result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI
root.mainloop()
