import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Advanced Widgets & Controls Exercise")
root.geometry("600x750")

personal_frame = tk.LabelFrame(root, text="Personal Information", padx=15, pady=15)
personal_frame.pack(fill="x", padx=20, pady=10)

tk.Label(personal_frame, text="Full Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(personal_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

gender_var = tk.StringVar(value="Male")
tk.Radiobutton(personal_frame, text="Male", variable=gender_var, value="Male").grid(row=1, column=0, sticky="w")
tk.Radiobutton(personal_frame, text="Female", variable=gender_var, value="Female").grid(row=1, column=1, sticky="w")

academic_frame = tk.LabelFrame(root, text="Academic Details", padx=15, pady=15)
academic_frame.pack(fill="x", padx=20, pady=10)

tk.Label(academic_frame, text="Department:").grid(row=0, column=0, sticky="w")
dept_combobox = ttk.Combobox(academic_frame, values=["Software Engineering", "Information Technology", "Information Systems"], state="readonly")
dept_combobox.current(0)
dept_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(academic_frame, text="Experience Level:").grid(row=1, column=0, sticky="w")
exp_scale = tk.Scale(academic_frame, from_=1, to=5, resolution=1, orient="horizontal")
exp_scale.set(1)
exp_scale.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

pref_frame = tk.LabelFrame(root, text="Preferences", padx=15, pady=15)
pref_frame.pack(fill="x", padx=20, pady=10)

email_notifications = tk.BooleanVar(value=True)
tk.Checkbutton(pref_frame, text="Enable Email Notifications", variable=email_notifications).pack(anchor="w")

mode_var = tk.StringVar(value="disabled")
tk.Checkbutton(pref_frame, text="Enable Advanced Beta Features", variable=mode_var, onvalue="enabled", offvalue="disabled").pack(anchor="w")

list_frame = tk.LabelFrame(root, text="Course Selection (Hold Ctrl to select multiple)", padx=15, pady=15)
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

scroll = tk.Scrollbar(list_frame)
scroll.pack(side="right", fill="y")

course_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED, yscrollcommand=scroll.set)
course_listbox.pack(side="left", fill="both", expand=True)
scroll.config(command=course_listbox.yview)

course_names = ["Python Programming", "Database Systems", "Computer Networking", "Web Development", "Artificial Intelligence", "Cyber Security"]
for course in course_names:
    course_listbox.insert(tk.END, course)

text_frame = tk.LabelFrame(root, text="Submitted Data Log", padx=15, pady=15)
text_frame.pack(fill="both", expand=True, padx=20, pady=10)

t_scroll = tk.Scrollbar(text_frame)
t_scroll.pack(side="right", fill="y")

log_text = tk.Text(text_frame, height=6, yscrollcommand=t_scroll.set)
log_text.pack(side="left", fill="both", expand=True)
t_scroll.config(command=log_text.yview)

def submit_form():
    log_text.delete("1.0", tk.END)
    log_text.insert(tk.END, f"Name: {name_entry.get()}\n")
    log_text.insert(tk.END, f"Gender: {gender_var.get()}\n")
    log_text.insert(tk.END, f"Department: {dept_combobox.get()}\n")
    log_text.insert(tk.END, f"Experience Level: {exp_scale.get()}\n")
    log_text.insert(tk.END, f"Email Notifications: {email_notifications.get()}\n")
    log_text.insert(tk.END, f"Beta Mode: {mode_var.get()}\n")
    
    selected_courses = [course_listbox.get(i) for i in course_listbox.curselection()]
    log_text.insert(tk.END, f"Selected Courses: {', '.join(selected_courses)}\n")

def reset_form():
    name_entry.delete(0, tk.END)
    gender_var.set("Male")
    dept_combobox.current(0)
    exp_scale.set(1)
    email_notifications.set(True)
    mode_var.set("disabled")
    course_listbox.selection_clear(0, tk.END)
    log_text.delete("1.0", tk.END)

btn_frame = tk.Frame(root)
btn_frame.pack(fill="x", padx=20, pady=5)

tk.Button(btn_frame, text="Submit", command=submit_form).pack(side="left", padx=5, pady=5)
tk.Button(btn_frame, text="Reset", command=reset_form).pack(side="left", padx=5, pady=5)

root.mainloop()