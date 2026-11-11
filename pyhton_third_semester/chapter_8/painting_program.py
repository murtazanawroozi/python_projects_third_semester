import tkinter as tk

root = tk.Tk()
root.title("Paint Exercise")

canvas = tk.Canvas(root, width=600, height=400, background="white")
canvas.pack(fill="both", expand=True)

last_x, last_y = None, None
current_color = "black"

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=3)
        last_x, last_y = event.x, event.y

def change_color(color):
    global current_color
    current_color = color

def clear_canvas(event):
    canvas.delete("all")

controls = tk.Frame(root)
controls.pack(fill="x")

tk.Button(controls, text="Red", command=lambda: change_color("red")).pack(side="left", padx=5, pady=5)
tk.Button(controls, text="Green", command=lambda: change_color("green")).pack(side="left", padx=5, pady=5)
tk.Button(controls, text="Blue", command=lambda: change_color("blue")).pack(side="left", padx=5, pady=5)
tk.Button(controls, text="Black", command=lambda: change_color("black")).pack(side="left", padx=5, pady=5)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
root.bind("<Escape>", clear_canvas)

root.mainloop()