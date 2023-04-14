from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    user_input = float(input.get())
    user_conversion = user_input * 1.609
    conversion.config(text=user_conversion)
    input.delete(1, 0)


# Entry
input = Entry(width=10)
input.grid(column=2, row=1)

# Label
miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=3, row=1)


equal = Label(text="is equal to", font=("Arial", 10, "bold"))
equal.grid(column=1, row=2)

kilometres = Label(text="Km", font=("Arial", 10, "bold"))
kilometres.grid(column=3, row=2)

conversion = Label(text="0", font=("Arial", 10, "bold"))
conversion.grid(column=2, row=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
