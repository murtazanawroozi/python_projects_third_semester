import tkinter as tk
from tkinter import font

def lees_formulier():
    return {
        "student_id": id_entry.get().strip(),
        "name": name_entry.get().strip(),
        "email": email_entry.get().strip(),
        "notes": notes_text.get("1.0", "end-1c").strip()
    }

def valideer(data):
    if not data["student_id"]:
        return False, "Student ID is verplicht!"
    if not data["name"]:
        return False, "Naam is verplicht!"
    if "@" not in data["email"]:
        return False, "Ongeldig e-mailadres!"
    return True, ""

def opslaan():
    data = lees_formulier()
    valide, melding = valideer(data)
    if not valide:
        status_label.config(text=melding, fg="red")
        return
    status_label.config(text=f"Student '{data['name']}' succesvol opgeslagen.", fg="darkgreen")

def wis_formulier():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    notes_text.delete("1.0", tk.END)
    status_label.config(text="Formulier gewist.", fg="black")
    id_entry.focus_set()

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")

titel_font = font.Font(family="Arial", size=16, weight="bold")
label_font = font.Font(family="Arial", size=10)

header_frame = tk.Frame(root, pady=10)
header_frame.pack(fill="x")
tk.Label(header_frame, text="Studenten Registratie", font=titel_font).pack()

main_frame = tk.Frame(root, padx=20, pady=10)
main_frame.pack(fill="both", expand=True)
main_frame.columnconfigure(1, weight=1)

tk.Label(main_frame, text="Student ID:", font=label_font).grid(row=0, column=0, sticky="e", pady=5)
id_entry = tk.Entry(main_frame)
id_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

tk.Label(main_frame, text="Volledige Naam:", font=label_font).grid(row=1, column=0, sticky="e", pady=5)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

tk.Label(main_frame, text="E-mail:", font=label_font).grid(row=2, column=0, sticky="e", pady=5)
email_entry = tk.Entry(main_frame)
email_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

tk.Label(main_frame, text="Opmerkingen:", font=label_font).grid(row=3, column=0, sticky="ne", pady=5)
notes_text = tk.Text(main_frame, height=6, width=30, wrap="word")
notes_text.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

knop_frame = tk.Frame(root, pady=15)
knop_frame.pack(fill="x")

save_button = tk.Button(knop_frame, text="Opslaan", command=opslaan, width=12)
save_button.pack(side="left", padx=40)

clear_button = tk.Button(knop_frame, text="Wissen", command=wis_formulier, width=12)
clear_button.pack(side="right", padx=40)

status_frame = tk.Frame(root, bd=1, relief="sunken", pady=5)
status_frame.pack(fill="x", side="bottom")
status_label = tk.Label(status_frame, text="Gereed voor invoer...", font=("Arial", 9, "italic"))
status_label.pack(anchor="w", padx=10)

id_entry.focus_set()
root.mainloop()