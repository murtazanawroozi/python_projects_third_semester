import tkinter as tk

root = tk.Tk()
root.title("Advanced Programming - Lecture 8 Exercise")

canvas = tk.Canvas(root, width=700, height=400, background="white")
canvas.pack(fill="both", expand=True)

ball = canvas.create_oval(50, 50, 90, 90, fill="red")
player = canvas.create_rectangle(300, 300, 360, 320, fill="blue")

status = tk.Label(root, text="Status: Ready", bd=1, relief="sunken", anchor="w")
status.pack(side="bottom", fill="x")

dx, dy = 4, 3
speed = 4
running = False
job_id = None
selected = None
start_position = (50, 50, 90, 90)

def animate():
    global dx, dy, job_id
    if not running:
        return
    
    x1, y1, x2, y2 = canvas.coords(ball)
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    
    if x1 <= 0 or x2 >= w:
        dx = -dx
    if y1 <= 0 or y2 >= h:
        dy = -dy
        
    canvas.move(ball, dx * (speed / 4), dy * (speed / 4))
    job_id = root.after(20, animate)

def start():
    global running
    if not running:
        running = True
        status.config(text="Status: Running")
        animate()

def pause():
    global running
    running = False
    status.config(text="Status: Paused")

def stop():
    global job_id, running
    running = False
    if job_id is not None:
        root.after_cancel(job_id)
        job_id = None
    status.config(text="Status: Stopped")

def reset():
    stop()
    canvas.coords(ball, *start_position)
    status.config(text="Status: Reset")

def faster():
    global speed
    speed += 1
    status.config(text=f"Status: Speed Up ({speed})")

def slower():
    global speed
    speed = max(1, speed - 1)
    status.config(text=f"Status: Speed Down ({speed})")

def start_drag(event):
    global selected
    closest = canvas.find_closest(event.x, event.y)
    if closest:
        selected = closest[0]

def drag(event):
    if selected:
        x1, y1, x2, y2 = canvas.coords(selected)
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        canvas.move(selected, event.x - cx, event.y - cy)

def move_player(event):
    moves = {
        "Left": (-10, 0),
        "Right": (10, 0),
        "Up": (0, -10),
        "Down": (0, 10)
    }
    if event.keysym in moves:
        dx_p, dy_p = moves[event.keysym]
        canvas.move(player, dx_p, dy_p)

def escape_pressed(event):
    reset()

btn_frame = tk.Frame(root)
btn_frame.pack(fill="x")

tk.Button(btn_frame, text="Start", command=start).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Pause", command=pause).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Stop", command=stop).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Reset", command=reset).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Faster", command=faster).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Slower", command=slower).pack(side="left", padx=5, pady=5)

canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", drag)
root.bind("<KeyPress>", move_player)
root.bind("<Escape>", escape_pressed)

canvas.focus_set()

root.mainloop()