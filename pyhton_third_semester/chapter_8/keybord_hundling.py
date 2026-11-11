import tkinter as tk

root = tk.Tk()
root.title("Two-Player Control Exercise")

canvas = tk.Canvas(root, width=600, height=400, background="lightgray")
canvas.pack()

p1 = canvas.create_rectangle(100, 180, 140, 220, fill="red")
p2 = canvas.create_oval(460, 180, 500, 220, fill="blue")

def handle_keypress(event):
    key = event.keysym
    
    if key == "w":
        canvas.move(p1, 0, -15)
    elif key == "s":
        canvas.move(p1, 0, 15)
    elif key == "a":
        canvas.move(p1, -15, 0)
    elif key == "d":
        canvas.move(p1, 15, 0)
        
    if key == "Up":
        canvas.move(p2, 0, -15)
    elif key == "Down":
        canvas.move(p2, 0, 15)
    elif key == "Left":
        canvas.move(p2, -15, 0)
    elif key == "Right":
        canvas.move(p2, 15, 0)

root.bind("<KeyPress>", handle_keypress)
canvas.focus_set()

root.mainloop()