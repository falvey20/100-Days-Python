import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# --- TIMER RESET --- #
def reset_timer():
    window.after_cancel(timer)
    # Reset Title
    main_title.config(text="Timer")
    # Reset Timer
    canvas.itemconfig(timer_text, text="00:00")
    # Reset checks
    checkmarks.config(text="")

    global reps
    reps = 0


# --- TIMER MECHANISM --- #
def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 == 0:
        count_down(short_break_secs)
        main_title.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_secs)
        main_title.config(text="Long Break", fg=RED)
    else:
        count_down(work_secs)
        main_title.config(text="Work", fg=GREEN)

# --- COUNTDOWN MECHANISM --- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            checks += "✔"
        checkmarks.config(text=checks)


# --- UI SETUP --- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


main_title = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
main_title.grid(row=0, column=1)

start_btn = tkinter.Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
reset_btn.grid(row=2, column=2)

checkmarks = tkinter.Label(bg=YELLOW, fg=GREEN)
checkmarks.grid(row=3, column=1)

window.mainloop()
