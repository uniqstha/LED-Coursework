import sqlite3
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image,ImageTk

def insert():
    try:
        fullname.get()
        department.get()
        int(age.get())
        var.get()
        int(contact.get())
        address.get()
    except ValueError:
        messagebox.showinfo("Error", "Enter correct datatype in the entry boxes")
        root.destroy()
        os.system('employee.py')
    if var.get() == '' or fullname.get() == '' or department.get() == '' or age.get() == '' or address.get() == '' or contact.get() == '':
        messagebox.showinfo("Error", "Required information is not fulfilled")
    else:
        con = sqlite3.connect("EmployeeInfo.db")
        cur = con.cursor()
        cur.execute("INSERT INTO employees VALUES(:FullName,:Department, :Age, :Gender, :Contact, :Address)", {
            'FullName': fullname.get(),
            'Department': department.get(),
            'Age': age.get(),
            'Gender': var.get(),
            'Contact': contact.get(),
            'Address': address.get()
        })
        messagebox.showinfo("Employee", "Employee Added Sucessfully !")

        con.commit()
        con.close()
        root.destroy()
        os.system(('employee.py'))



def clear():
    fullname.delete(0,END)
    department.delete(0,END)
    age.delete(0,END)
    gender.delete(0,END)
    contact.delete(0,END)
    address.delete(0, END)


def add():
    global root
    root = Toplevel()
    root.geometry("1366x768")
    root.title("Add Employee")
    root.iconbitmap('./images/4.ico')
    myimage1 = ImageTk.PhotoImage(Image.open('./images/add.png'))
    label1 = Label(root, image=myimage1)
    label1.pack()

    global fullname
    global department
    global age
    global var
    global contact
    global address

    # desgin
    root.geometry("1366x768+60+10")
    root.resizable(0, 0)

    fullname_lbl = Label(root, text="Full Name", font=('Consolas', 15), bg="white")
    fullname_lbl.place(x=180, y=200)
    department_lbl = Label(root, text="Department", font=('Consolas', 15), bg="white")
    department_lbl.place(x=720, y=200)
    age_lbl = Label(root, text="Age", font=('Consolas', 15), bg="white")
    age_lbl.place(x=180, y=290)
    gender_lbl = Label(root, text="Gender", font=('Consolas', 15), bg="white")
    gender_lbl.place(x=720, y=290)
    contact_lbl = Label(root, text="Contact", font=('Consolas', 15), bg="white")
    contact_lbl.place(x=180, y=380)
    address_lbl = Label(root, text="Address", font=('Consolas', 15), bg="white")
    address_lbl.place(x=720, y=380)

    fullname = Entry(root, width=40, border=0, font=('Consolas', 15))
    fullname.place(x=180, y=230)
    department = Entry(root, width=40, border=0, font=('Consolas', 15))
    department.place(x=720, y=230)
    age = Entry(root, width=40, border=0, font=('Consolas', 15))
    age.place(x=180, y=320)
    var = StringVar()
    r1 = Radiobutton(root, text="Male", value="Male", variable=var, tristatevalue=0,font=('Consolas', 13),bg="white")
    r1.place(x=720, y=320)
    r2 = Radiobutton(root, text="Female", value="Female", variable=var, tristatevalue=0,font=('Consolas', 13),bg="white")
    r2.place(x=800, y=320)
    r3 = Radiobutton(root, text="Other", value="Other", variable=var, tristatevalue=0,font=('Consolas', 13),bg="white")
    r3.place(x=900, y=320)

    contact = Entry(root, width=40, border=0, font=('Consolas', 15))
    contact.place(x=180, y=410)
    address = Entry(root, width=40, border=0, font=('Consolas', 15))
    address.place(x=720, y=410)
    add_btn = Button(root, text="ADD", font=('Consolas', 15), cursor='hand2',
                     bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command = insert)
    add_btn.place(x=560, y=630)
    clear_btn = Button(root, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                       bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command=clear)
    clear_btn.place(x=715, y=630)


    root.mainloop()