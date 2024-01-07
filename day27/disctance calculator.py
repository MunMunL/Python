from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def convert():
    km_output = round(float(miles_input.get()) * 1.60934)
    km_number.config(text=f"{km_output}")

#Input
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

#Labels
miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

equals_text = Label(text="is equal to")
equals_text.grid(column=0, row=1)

km_number = Label(text=0)
km_number.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

#Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()