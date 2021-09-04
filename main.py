from tkinter import *
import math
from PIL import Image, ImageTk

#---------------------------- CONSTANTS -------------------------------
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

#---------------------------- TIMER MECHANISM -------------------------
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #Canvas must be created first and then we can call count_down() otherwise the function will not work:
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW , font=(FONT_NAME, 45, "bold"))

    #Color changes depending on rep number
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

#---------------------------- TIMER RESET -----------------------------
def reset_timer():
    window.after_cancel(timer)
    #timer_text reset
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    #reset check_marks
    check_label.config(text="")
    #reset reps
    global reps
    reps = 0

#---------------------------- COUNTDOWN MECHANISM ---------------------
def count_down(count):
    #Return the largest whole number with math.floor()
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    #Canvas text modification with itemconfig() method.
    #itemconfig (exact item to configure, *kwargs)
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        #Windows after() method - Execute command after a time delay
        #after (delay in ms, function to pass, *args-positional arguments)
        #Put the method inside function so that it will repeat and call itself
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

#---------------------------- UI SETUP --------------------------------
window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
#Background setting
window.config(padx=50, pady=50, bg=YELLOW)

#Canvas object to add color/picture overlapping layers on screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#Read and resize logo
img = Image.open("tomato.png")
resized_image = img.resize((200, 220), Image.ANTIALIAS)
tomato_image = ImageTk.PhotoImage(resized_image)
#Add logo to canvas and setup
canvas.create_image(100, 112, image=tomato_image)

#Add text and change it on canvas
timer_text = canvas.create_text(103, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

#Labels
##Timer
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW , font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)
##Check marks
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
#Buttons
##Start
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
##Reset
reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
