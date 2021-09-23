from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
import tkinter as tk
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ReturnBook import returnBook
from ViewBooks import *
from IssueBook import *



def page_display():
    global  Canvas1, n, same, con, cur, root

    con = pymysql.connect(host="localhost", user="root", password="", database="db")
    # root is the username here

    cur = con.cursor()  # cur -> cursor

    root = Tk()
    root.config(bg="skyblue")
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")



    headingFrame1 = Frame(root, bg="#1500ff", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to Library", bg='black', fg='#1500ff',
                         font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Add Book", bg='black', fg='white', command=addBook)
    btn1.place(relx=0.20, rely=0.4, relwidth=0.35, relheight=0.08)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.53, rely=0.4, relwidth=0.35, relheight=0.08)

    btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
    btn3.place(relx=0.20, rely=0.6, relwidth=0.35, relheight=0.08)

    btn4 = Button(root, text="Issue Book", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.53, rely=0.6, relwidth=0.35, relheight=0.08)

    btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.20, rely=0.8, relwidth=0.35, relheight=0.08)

    btn6 = Button(root, text="Logout", bg='black', fg='white', command=root.destroy)
    btn6.place(relx=0.53, rely=0.8, relwidth=0.35, relheight=0.08)

    root.mainloop()