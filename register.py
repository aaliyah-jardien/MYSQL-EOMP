from tkinter import *

# WINDOW FEATURES
window = Tk()
window.title("Life Choices Online Register")
window.geometry("900x750")
window.config(bg="black")
window.resizable(0, 0)

# PICTURE
img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=900, height=215, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=-10, y=25)

# LABELS
# line1 = Label(text="Welcome to Life Choices Online!", bg="black", fg="white", font="arial 30 bold")
# line1.place(x=58, y=290)
# ENTRIES
# BUTTONS

window.mainloop()
