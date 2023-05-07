from tkinter import *


#Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Consolas", 16, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"  # you can change the "text" option like this or
my_label.config(text="New Text 2")  # or like this
my_label.config(padx=50, pady=50)

# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)

new_button = Button(text="New Button")
new_button.grid(column=0, row=2)


#Entry component

input = Entry(width=10)
input.grid(column=0, row=3)

window.mainloop()  # this will keep the window open and this has to in the end of the code
