from tkinter import *

# WINDOW FEATURES
window = Tk()
window.title("Life Choices Online Login")
window.geometry("900x650")
window.config(bg="black")
window.resizable(0, 0)

# PICTURE
img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=900, height=215, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=-10, y=25)

window.mainloop()
