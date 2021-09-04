from tkinter import *

#---------------------------- CONSTANTS -------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

#---------------------------- UI SETUP --------------------------------
window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
#Background setting
window.config(padx=50, pady=50, bg=YELLOW)

#Canvas object to add color/picture overlapping layers on screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#Read logo
tomato_image = PhotoImage(file="tomato.png")
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
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 14, "bold"))
start_button.grid(column=0, row=2)
##Reset
reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=2)

window.mainloop()
