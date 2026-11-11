import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Event Exercise")
root.geometry("400x200")

label_frame = tk.LabelFrame(root, text="Select Theme", padx=15, pady=15)
label_frame.pack(fill="both", expand=True, padx=20, pady=20)

theme_label = tk.Label(label_frame, text="Current Style: Light Mode")
theme_label.pack(pady=10)

theme_combobox = ttk.Combobox(label_frame, values=["Light Mode", "Dark Mode", "Blue Ocean"], state="readonly")
theme_combobox.current(0)
theme_combobox.pack(pady=5)

def update_theme(event):
    selected = theme_combobox.get()
    theme_label.config(text=f"Current Style: {selected}")
    
    if selected == "Light Mode":
        label_frame.config(background="white", foreground="black")
        theme_label.config(background="white", foreground="black")
    elif selected == "Dark Mode":
        label_frame.config(background="#333333", foreground="white")
        theme_label.config(background="#333333", foreground="white")
    elif selected == "Blue Ocean":
        label_frame.config(background="#e0f7fa", foreground="#006064")
        theme_label.config(background="#e0f7fa", foreground="#006064")

theme_combobox.bind("<<ComboboxSelected>>", update_theme)

root.mainloop()