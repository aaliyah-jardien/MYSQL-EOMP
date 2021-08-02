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

# ENTRIES
name = Label(window, text="Name:", bg="black", fg="white", font="arial 15 bold", border="10")
name.place(x=35, y=250)

surname = Label(window, text="Surname:", bg="black", fg="white", font="arial 15 bold", border="10")
surname.place(x=450, y=250)

id = Label(window, text="ID:", bg="black", fg="white", font="arial 15 bold", border="10")
id.place(x=35, y=350)

email = Label(window, text="Email:", bg="black", fg="white", font="arial 15 bold", border="10")
email.place(x=450, y=350)

phone = Label(window, text="Phone:", bg="black", fg="white", font="arial 15 bold", border="10")
phone.place(x=35, y=440)

role = Label(window, text="Role:", bg="black", fg="white", font="arial 15 bold", border="10")
role.place(x=450, y=440)

password = Label(window, text="Password:", bg="black", fg="white", font="arial 15 bold", border="10")
password.place(x=35, y=550)

confirm = Label(window,text=" Confirm Password:", bg="black", fg="white", font="arial 15 bold", border="10")
confirm.place(x=450, y=550)

# ENTRIES

window.mainloop()
