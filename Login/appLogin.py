from tkinter import *

user = "admin"
passw = "admin"

def login():
    if userName.get() == user and paswd.get() == passw:
        print("Login Berhasil")
    else:
        print("Login Gagal")


# Membuat Entry dengan placeholder
def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg='grey')  # warna placeholder

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, END)
            entry.config(fg='white')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, text)
            entry.config(fg='grey')

    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)

# membuat windownya
root = Tk()
root.title("Login Admin")
root.geometry("300x300")

#membuat Label
label = Label(root, text="Login Admin")
label.pack()

# Entry Username
userName = Entry(root)
userName.pack(pady=10)
add_placeholder(userName, "User Name")

# Entry Password
paswd = Entry(root, show="*")
paswd.pack(pady=10)
add_placeholder(paswd, "Password")

# membuat tombol
button = Button(root, text="Login", command = login)
button.pack()

root.mainloop()