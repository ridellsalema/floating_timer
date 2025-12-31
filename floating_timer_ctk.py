import customtkinter as ctk
import time

# ---------------- CONFIG ----------------
ctk.set_appearance_mode("light")   # "dark" or "light"
ctk.set_default_color_theme("blue")

# ---------------- WINDOW ----------------
root = ctk.CTk()
root.geometry("260x90")
root.overrideredirect(True)            # borderless
root.attributes("-topmost", True)      # always on top

# ---------------- TIMER STATE ----------------
start_time = time.time()
paused = False
pause_start = 0
total_paused = 0

# ---------------- TIMER UPDATE ----------------
def update_timer():
    if not paused:
        elapsed = int(time.time() - start_time - total_paused)

        h = elapsed // 3600
        m = (elapsed % 3600) // 60
        s = elapsed % 60

        timer_label.configure(text=f"{h:02}:{m:02}:{s:02}")

    root.after(1000, update_timer)



# ---------------- UI ----------------
container = ctk.CTkFrame(
    root,
    corner_radius=18,
    fg_color="#F54927"
)
container.pack(fill="both", expand=True, padx=6, pady=6)

timer_label = ctk.CTkLabel(
    container,
    text="00:00:00",
    font=ctk.CTkFont(
        family="impact",
        size=34
    ),
    text_color="#111111"
)
timer_label.pack(expand=True)

# ---------------- DRAG WINDOW ----------------
def start_drag(event):
    root.x = event.x_root
    root.y = event.y_root

def drag(event):
    dx = event.x_root - root.x
    dy = event.y_root - root.y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")
    root.x = event.x_root
    root.y = event.y_root

container.bind("<Button-1>", start_drag)
container.bind("<B1-Motion>", drag)

# ---------------- CONTROLS ----------------
def toggle_pause(event=None):
    global paused, pause_start, total_paused
    if not paused:
        paused = True
        pause_start = time.time()
    else:
        paused = False
        total_paused += time.time() - pause_start

def restart_timer(event=None):
    global start_time, paused, total_paused, pause_start

    start_time = time.time()
    total_paused = 0
    pause_start = 0
    paused = False

    timer_label.configure(text="00:00:00")


root.bind("<space>", toggle_pause)
root.bind("<BackSpace>", restart_timer)
root.bind("<Escape>", lambda e: root.destroy())

update_timer()
root.mainloop()
