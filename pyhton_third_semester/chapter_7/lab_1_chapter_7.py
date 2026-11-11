import tkinter as tk

def focus_in(event):
    event.widget.config(background="lightyellow")

def focus_out(event):
    event.widget.config(background="white")

def verwerk_invoer(event=None):
    tekst = invoer_veld.get().strip()
    if not tekst:
        status_label.config(text="Invoer mag niet leeg zijn!", fg="red")
    else:
        status_label.config(text=f"Opgeslagen: {tekst}", fg="darkgreen")

def sluit_applicatie():
    print("Applicatie wordt veilig afgesloten.")
    root.destroy()

root = tk.Tk()
root.title("Event interactie Formulier")
root.geometry("400x200")

root.protocol("WM_DELETE_WINDOW", sluit_applicatie)

tk.Label(root, text="Typ uw invoer en druk op Enter of Ctrl+S:").pack(pady=10)

invoer_veld = tk.Entry(root, width=30)
invoer_veld.pack(pady=5)

invoer_veld.bind("<FocusIn>", focus_in)
invoer_veld.bind("<FocusOut>", focus_out)
invoer_veld.bind("<Return>", verwerk_invoer)

root.bind("<Control-s>", verwerk_invoer)
root.bind("<Control-S>", verwerk_invoer)

status_label = tk.Label(root, text="Wachten op actie...", font=("Arial", 10, "italic"))
status_label.pack(pady=20)

invoer_veld.focus_set()
root.mainloop()