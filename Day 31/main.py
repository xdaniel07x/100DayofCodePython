from tkinter import messagebox
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="Day 31\images\card_front.png")
canvas.create_image(410, 270, image=card_img)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="French", font=(
    "Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=(
    "Ariel", 60, "bold"))


# Buttons

wrong_image = PhotoImage(file="Day 31\images\wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0,
                      bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

correct_image = PhotoImage(file="Day 31\images\correct.png")
correct_button = Button(image=correct_image,
                        borderwidth=0, bg=BACKGROUND_COLOR)
correct_button.grid(row=1, column=1)

window.mainloop()
