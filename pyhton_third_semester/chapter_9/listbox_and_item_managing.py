import tkinter as tk

root = tk.Tk()
root.title("Dynamic Listbox Exercise")
root.geometry("400x400")

input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill="x")

item_entry = tk.Entry(input_frame)
item_entry.pack(side="left", fill="x", expand=True, padx=5)

list_frame = tk.LabelFrame(root, text="Your Shopping List", padx=10, pady=10)
list_frame.pack(fill="both", expand=True, padx=15, pady=5)

scroll = tk.Scrollbar(list_frame)
scroll.pack(side="right", fill="y")

item_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, yscrollcommand=scroll.set)
item_listbox.pack(side="left", fill="both", expand=True)
scroll.config(command=item_listbox.yview)

counter_label = tk.Label(root, text="Total Items: 0", anchor="w", padx=15)
counter_label.pack(fill="x", side="bottom", pady=5)

def update_counter():
    counter_label.config(text=f"Total Items: {item_listbox.size()}")

def add_item():
    text = item_entry.get().strip()
    if text:
        item_listbox.insert(tk.END, text)
        item_entry.delete(0, tk.END)
        update_counter()

def remove_item():
    selected = item_listbox.curselection()
    if selected:
        item_listbox.delete(selected[0])
        update_counter()

tk.Button(input_frame, text="Add Item", command=add_item).pack(side="right", padx=5)
tk.Button(root, text="Delete Selected Item", command=remove_item).pack(fill="x", padx=15, pady=5)

root.mainloop()