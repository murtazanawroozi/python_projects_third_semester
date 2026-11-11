import tkinter as tk

def bereken_celsius():
    try:
        fahrenheit = float(fahrenheit_veld.get())
        celsius = (fahrenheit - 32) * 5 / 9
        resultaat_label.config(text=f"{celsius:.2f} °C", fg="black")
    except ValueError:
        resultaat_label.config(text="Fout: Voer een geldig getal in.", fg="red")

root = tk.Tk()
root.title("Temperatuur Converter")
root.geometry("350x180")
root.minsize(300, 150)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=15, pady=15, sticky="e")
fahrenheit_veld = tk.Entry(root)
fahrenheit_veld.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

bereken_knop = tk.Button(root, text="Bereken Celsius", command=bereken_celsius)
bereken_knop.grid(row=1, column=0, columnspan=2, pady=10)

resultaat_label = tk.Label(root, text="0.00 °C", font=("Arial", 14, "bold"))
resultaat_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()