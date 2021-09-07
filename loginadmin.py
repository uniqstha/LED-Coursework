from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import os
root=Tk()
root.title("Admin Login")
root.geometry("1366x768+60+10")
root.resizable(0, 0)
root.iconbitmap('./images/3.ico')

#assigning e1 and e2 as global variable
global e1
global e2

#functions used in loginadmin.py
def ok():
    uname=e1.get()
    password=e2.get()
    if(uname==""and password==""):
        messagebox.showinfo("Login", "Enter Username and Password")
    elif(uname=="admin"and password=="admin"):
        messagebox.showinfo("Login Success", "Login Successfully!")
        root.withdraw()
        os.system("admin.py")
    else:
        messagebox.showinfo("Login Failed", "Username or Password invalid.Try Again!")

#design for the login admin window
myimage=ImageTk.PhotoImage(Image.open('./images/adminlogin.png'))
Label(image=myimage).pack()
#e1 entry for username entry
e1=Entry(root,width=40,border=0,font=('Consolas',13))
e1.place(x=510,y=210)

#e2 entry for password entry
e2=Entry(root,width=40,border=0,show='*',font=('Consolas',13))
e2.place(x=510,y=300)

Button(root,text='LOGIN',font=('Consolas',20), padx=20,pady=10,cursor='hand2',border=0,bg="#6dcff6",
       activebackground="#6dcff6",command=ok).place(x=625,y=515)
root.mainloop()