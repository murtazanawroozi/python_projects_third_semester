import tkinter as tk

def voeg_toe():
    naam = naam_var.get().strip()
    try:
        aantal = aantal_var.get()
    except tk.TclError:
        status_lbl.config(text="Fout: Aantal moet een cijfer zijn!", fg="red")
        return

    if not naam:
        status_lbl.config(text="Fout: Productnaam mag niet leeg zijn!", fg="red")
        return
    if aantal <= 0:
        status_lbl.config(text="Fout: Aantal moet groter zijn dan 0!", fg="red")
        return

    log_text.config(state="normal")
    log_text.insert(tk.END, f"- {aantal}x {naam}\n")
    log_text.config(state="disabled")

    naam_var.set("")
    aantal_var.set(1)
    status_lbl.config(text="Product toegevoegd aan logboek.", fg="darkgreen")
    naam_entry.focus_set()

root = tk.Tk()
root.title("Product Inventaris Log")
root.geometry("420x400")

naam_var = tk.StringVar()
aantal_var = tk.IntVar(value=1)

input_frame = tk.Frame(root, padx=15, pady=15)
input_frame.pack(fill="x")
input_frame.columnconfigure(1, weight=1)

tk.Label(input_frame, text="Product Naam:").grid(row=0, column=0, sticky="e", pady=5)
naam_entry = tk.Entry(input_frame, textvariable=naam_var)
naam_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

tk.Label(input_frame, text="Aantal:").grid(row=1, column=0, sticky="e", pady=5)
aantal_entry = tk.Entry(input_frame, textvariable=aantal_var)
aantal_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

add_btn = tk.Button(root, text="Voeg toe aan Log", command=voeg_toe)
add_btn.pack(pady=5)

status_lbl = tk.Label(root, text="Voer een product in...", font=("Arial", 9, "italic"))
status_lbl.pack(pady=5)

tk.Label(root, text="Historie:", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=5)

log_text = tk.Text(root, height=10, width=45, state="disabled", wrap="word")
log_text.pack(padx=15, pady=10, fill="both", expand=True)

naam_entry.focus_set()
root.mainloop()