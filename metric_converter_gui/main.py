import tkinter

window = tkinter.Tk()
window.title("Baby's First GUI")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked(label=my_label):
    label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry()
input.config(width=50)
input.pack()


window.mainloop()
