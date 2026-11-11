import tkinter as tk

def controleer_inloggen():
    ingevoerde_naam = gebruikersnaam_veld.get()
    if ingevoerde_naam == "admin":
        status_label.config(text="Inloggen succesvol!", fg="green")
    else:
        status_label.config(text="Onjuiste inloggegevens.", fg="red")

root = tk.Tk()
root.title("Beveiligd Systeem")
root.geometry("400x250")

formulier_frame = tk.Frame(root, padx=20, pady=20)
formulier_frame.pack()

tk.Label(formulier_frame, text="Gebruikersnaam:").grid(row=0, column=0, sticky="e", pady=5)
gebruikersnaam_veld = tk.Entry(formulier_frame, width=25)
gebruikersnaam_veld.grid(row=0, column=1, padx=8, pady=5)

tk.Label(formulier_frame, text="Wachtwoord:").grid(row=1, column=0, sticky="e", pady=5)
wachtwoord_veld = tk.Entry(formulier_frame, width=25, show="*")
wachtwoord_veld.grid(row=1, column=1, padx=8, pady=5)

inlog_knop = tk.Button(formulier_frame, text="Inloggen", command=controleer_inloggen)
inlog_knop.grid(row=2, column=0, columnspan=2, pady=15)

status_label = tk.Label(root, text="Vul uw gegevens in...", font=("Arial", 10, "italic"))
status_label.pack(pady=5)

root.mainloop()