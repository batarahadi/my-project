from tkinter import *

# membuat windownya
root = Tk()
root.title("Login Admin")
root.geometry("300x300")

user = "admin"
passw = "admin"

def login():
    if userName.get() == user and paswd.get() == passw:
        print("Login Berhasil")
    else:
        print("Login Gagal")

#membuat Label
label = Label(root, text="Login Admin")
label.pack()

#membuat inputan
userName = Entry(root, text="Username")
# userName.insert(0,"User Name")
userName.pack()

paswd = Entry(root, text="Password", show="*")
# paswd.insert(0,"Password")
paswd.pack()

# membuat tombol
button = Button(root, text="Login", command = login)
button.pack()

root.mainloop()