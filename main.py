from tkinter import *


root = Tk()
root.title("Login Admin")
root.geometry("300x300")

#membuat Label
label = Label(root, text="Login Admin")
label.pack()

#membuat inputan
userName = Entry(root)
userName.pack()

paswd = Entry(root)
paswd.pack()

# membuat tombol
button = Button(root, text="Login")
button.pack()

root.mainloop()