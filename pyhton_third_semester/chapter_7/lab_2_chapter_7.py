import tkinter as tk

def update_muis_positie(event):
    coordinaten_label.config(text=f"Muis positie: X = {event.x}, Y = {event.y}")

def update_timer():
    global teller
    teller += 1
    timer_label.config(text=f"Tijd verstreken: {teller} seconden")
    root.after(1000, update_timer)

root = tk.Tk()
root.title("Muis Tracker en Live Timer")
root.geometry("400x250")

teller = 0

instructie_label = tk.Label(root, text="Beweeg uw muis over het venster", font=("Arial", 12, "bold"))
instructie_label.pack(pady=15)

coordinaten_label = tk.Label(root, text="Muis positie: X = 0, Y = 0", font=("Arial", 11))
coordinaten_label.pack(pady=15)

timer_label = tk.Label(root, text="Tijd verstreken: 0 seconden", font=("Arial", 11, "italic"), fg="blue")
timer_label.pack(pady=15)

root.bind("<Motion>", update_muis_positie)

update_timer()

root.mainloop()