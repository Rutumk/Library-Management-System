from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
import tkinter as tk
from tkinter import messagebox
from entry_page import *


con = pymysql.connect(host="localhost", user="root", password="", database="db")
    # root is the username here

cur = con.cursor()  # cur -> cursor

root = Tk()

logTable = "login"

root.title("Login System")
root.geometry("750x500")


same = True
n = 2.5

# Adding a background image
background_image = Image.open('img//library.jpg')
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
img1 = Label(root, image = img)
img1.place(x = 0, y = 50)


def log():
    global root2
    root2=Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification

    Label(root2, text='Login', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white", bg="blue", width=300).pack()

    username_verification = StringVar()
    password_verification = StringVar()

    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable = username_verification).pack()

    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable = password_verification, show="*").pack()

    Label(root2, text="").pack()

    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command = login_verification).pack()
    Label(root2, text="")




def failed_destroy():
    failed_message.destroy()



def failed():
    global failed_message
    failed_message = Toplevel(root)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from " + logTable + " where user_name = %s and password = %s "
    cur.execute(sql, [(user_verification), (pass_verification)])
    results=cur.fetchall()
    if results:
        for i in results:
            page_display()
            break
    else:
        failed()

def Registration():
    global root3, Userinfo, Passinfo, CPassinfo
    root3 = Toplevel(root)
    root3.geometry('500x500')
    root3.title("Registration")

    Label(root3, text='Registration', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white", bg="blue", width=300).pack()

    label1 = Label(root3, text="Username:", width=20, font=("bold", 10))
    label1.place(relx=0.05, rely=0.2, relheight=0.08)

    Userinfo = Entry(root3)
    Userinfo.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    label2 = Label(root3, text="Password:", width=20, font=("bold", 10))
    label2.place(relx=0.05, rely=0.35, relheight=0.08)

    Passinfo = Entry(root3, show="*")
    Passinfo.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    label3 = Label(root3, text="Confirm Password:", width=20, font=("bold", 10))
    label3.place(relx=0.02, rely=0.50, relheight=0.08)

    CPassinfo = Entry(root3, show="*")
    CPassinfo.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)


    Button(root3, text='Submit', width=20, bg='blue', fg='white', command=reginfo).place(relx=0.4, rely=0.75, relwidth=0.18, relheight=0.08)


def reginfo():
    username = Userinfo.get()
    password = Passinfo.get()
    cpass = CPassinfo.get()

    if cpass == password:
        insertReg = "insert into " + logTable + " values ('" + username + "','" + password + "')"
        cur.execute(insertReg)
        con.commit()
        messagebox.showinfo('Success', "Registration done  successfully")

        print(username)
        print(password)
        root3.destroy()
    else:
        messagebox.showinfo("Error", "Check password")


def main_display():


    Label(root, text='Welcome to Library Log In', bd=20, font=('arial', 20, 'bold'),  relief="groove", fg="white",
          bg="black", width=100).pack()

    Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=log).pack()
    Label(root, text="").pack()

    Button(root, text='Register', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=Registration).pack()
    Label(root, text="").pack()

    Button(root, text='Exit', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="red", command=root.destroy).pack()
    Label(root, text="").pack()


main_display()
root.mainloop()


