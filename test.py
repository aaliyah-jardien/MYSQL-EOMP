# Aaliyah
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class login:
    def __init__(self, window):
        self.window = window
        self.window.title("Life Choices Online")
        self.window.geometry("900x700")
        self.window.config(bg="black")
        self.window.resizable(0, 0)

        # self.window.img = PhotoImage(file="logo.png")
        # self.window.canvas = Canvas(window, width=900, height=215, highlightthickness="0")
        # self.window.canvas.create_image(0, 0, anchor=NW, image=img)
        # self.window.canvas.place(x=-10, y=25)

        self.line1 = Label(text="Welcome to Life Choices Online!", bg="black", fg="white", font="arial 30 bold")
        self.line1.place(x=58, y=290)
        self.line2 = Label(text="To proceed, please select your choice below.", bg="black", fg="#A5D200", font="arial 21 italic")
        self.line2.place(x=95, y=355)
        self.sign = Label(text="Designed by Aaliyah Jardien ©", bg="black", fg="white", font="arial 12 bold")
        self.sign.place(x=275, y=640)


if __name__ == "__main__":
    window = Tk()
    application = login(window)
    window.mainloop()

