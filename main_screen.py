from tkinter import *

# WINDOW FEATURES
window = Tk()
window.title("Life Choices Online")
window.geometry("900x650")
window.config(bg="black")
window.resizable(0, 0)

# PICTURE
img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=900, height=215, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=-10, y=25)

# LABELS
line1 = Label(text="Welcome to Life Choices Online!", bg="black", fg="white", font="arial 30 bold")
line1.place(x=58, y=290)

line2 = Label(text="To proceed, please select your choice below.", bg="black", fg="#A5D200", font="arial 21 italic")
line2.place(x=95, y=355)

# FUNCTIONS
# def log

# BUTTONS
regis = Button(text="Register", command="", bg="#6B8213", fg="white", font="arial 25 bold", border="10")
regis.place(x=70, y=490)

login = Button(text="Login", command="", bg="#6B8213", fg="white", font="arial 25 bold", border="10")
login.place(x=385, y=490)

admin = Button(text="Admin", command="", bg="#6B8213", fg="white", font="arial 25 bold", border="10")
admin.place(x=650, y=490)


window.mainloop()
