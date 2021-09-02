from tkinter import *
import os
#creating root window
root = Tk()
root.lift()
root.geometry("1366x768+60+10")
root.title("Login Page")
root.resizable(0, 0)

def emp_login():
    root.withdraw()
    os.system("loginemp.py")
    root.deiconify()


label1 = Label(root)
label1.place(x=0, y=0, width=1366, height=768)
img = PhotoImage(file="./images/loginas.png")
label1.configure(image=img)

button1 = Button(root,bg='white',fg='white',activebackground="white",relief="flat",overrelief="flat",borderwidth="0",
                 cursor='hand2',command=emp_login)
button1.place(x=430,y=330, width=146, height=90)
img2 = PhotoImage(file="./images/employee_icon.png")
button1.configure(image=img2)
Label(root,text='EMPLOYEE',bg='white',font=('Consolas',15)).place(x=455,y=410)


button2 = Button(root,bg='white',fg='white',activebackground="white",relief="flat",overrelief="flat",borderwidth="0",
                 cursor='hand2')
button2.place(x=774,y=330, width=146, height=100)
img3 = PhotoImage(file="./images/admin_icon.png")
button2.configure(image=img3)
Label(root,text='ADMIN',bg='white',font=('Consolas',15)).place(x=815,y=410)


root.mainloop()

