import tkinter


def calc_km():
    text = float(miles_entry.get()) * 1.609
    km_entry.delete(0, tkinter.END)
    km_entry.insert(0, f"{round(text,2)}")


def calc_miles():
    text = float(km_entry.get()) / 1.609
    miles_entry.delete(0, tkinter.END)
    miles_entry.insert(0, f"{round(text,2)}")


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=10, pady=10)
# window.minsize(width=300, height=200)


# Text Boxes
miles = tkinter.Label(text="Miles", anchor="w")
miles.grid(column=2, row=0)

equal_to = tkinter.Label(text="is equal to")
equal_to.grid(column=0, row=1)

km = tkinter.Label(text="KM", anchor="w")
km.grid(column=2, row=1)

# Entries
miles_entry = tkinter.Entry(width=15)
miles_entry.grid(column=1, row=0)

km_entry = tkinter.Entry(width=15)
km_entry.grid(column=1, row=1)

# Buttons
miles_button = tkinter.Button(text="Calculate Miles", command=calc_miles)
miles_button.grid(column=0, row=4)

km_button = tkinter.Button(text="Calculate KM", command=calc_km)
km_button.grid(column=1, row=4)

tkinter.mainloop()
