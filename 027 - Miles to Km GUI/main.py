import tkinter
from tkinter import END


def calculate_km():
    converted = round(float(mile_input.get()) * 1.609)
    conversion_result["text"] = converted


# Set Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=50)

# User input
mile_input = tkinter.Entry(width=5)
mile_input.grid(column=1, row=0)
mile_input.insert(END, string="0")

# Mile Label
mile_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)

# Km Label
km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# Is equal text
is_equal_text = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_text.grid(column=0, row=1)

# Button
my_button = tkinter.Button(text="Click Me", command=calculate_km)
my_button.grid(column=1, row=2)

# Result Text
conversion_result = tkinter.Label(text="0", font=("Arial", 12, "bold"))
conversion_result.grid(column=1, row=1)


window.mainloop()
