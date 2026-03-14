import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    if timer is not None:
        window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tracker_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN, bg=YELLOW)

def reset_and_start_timer():
    reset_timer()
    start_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def update_tracker():
    marks = ""
    for i in range(math.floor(reps/2)):
        marks += CHECKMARK
    tracker_label.config(text=marks)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_tracker()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", bg=YELLOW, highlightthickness=0, borderwidth=0, highlightbackground=YELLOW, command=reset_and_start_timer)
start_button.grid(row=2, column=0)

tracker_label = tk.Label(text="", fg=GREEN, bg=YELLOW)
tracker_label.grid(row=2, column=1)

reset_button = tk.Button(text="Reset", highlightthickness=0, borderwidth=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
