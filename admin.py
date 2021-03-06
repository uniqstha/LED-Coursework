from tkinter import *
from PIL import Image,ImageTk
import os
import addadmin
import sqlite3
from tkinter import messagebox
from tkinter import ttk

#creating GUI window for admin management window
root=Tk()
root.geometry("1366x768+60+10")
root.title("Administration Management")
root.resizable(0, 0)
root.iconbitmap('./images/3.ico')

# functions used in admin management window
def delete():
    if (employeeID.get()==""):
        messagebox.showinfo("Error","Please select employee")
    else:

        conn = sqlite3.connect('EmployeeInfo.db')
        c = conn.cursor()
        c.execute('DELETE from employees WHERE oid= ' + employeeID.get())
        messagebox.showinfo("Delete", "Deleted Successfully!")
        root.withdraw()
        conn.commit()
        conn.close()
        employeeID.delete(0, END)
        os.system("admin.py")

def search():
    if (employeeID.get() == ""):
        messagebox.showinfo("Error", "Enter FullName in Entry ID to search")
    else:
        record_id = employeeID.get()
        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect("EmployeeInfo.db")
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM employees WHERE FullName = ?", (record_id,))
        records = c.fetchall()

        for record in records:
            my_tree.insert('', 'end', values=(record))

        conn.commit()
        conn.close()


def adding():
    root.withdraw()
    addadmin.add()

def save():
    global main
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
        os.system('admin.py')
    if var.get() == '' or fullname.get() == '' or department.get() == '' or age.get() == '' or address.get() == '' or contact.get() == '':
        messagebox.showinfo("Error", "Required information is not fulfilled")
    else:
        conn = sqlite3.connect('EmployeeInfo.db')
        c = conn.cursor()
        record_id = employeeID.get()
        c.execute("""UPDATE employees SET
                FullName=:fullname,
                Department=:department,
                Age=:age,
                Gender=:gender,
                Contact=:contact,
                Address=:address
                WHERE oid =:oid""",
                  {
                      'fullname': fullname.get(),
                      'department': department.get(),
                      'age': age.get(),
                      'gender': var.get(),
                      'contact': contact.get(),
                      'address': address.get(),
                      'oid': record_id
                  })
        conn.commit()
        conn.close()
        employeeID.delete(0, END)
        messagebox.showinfo("Update", "Information Updated Succesfully")
        main.destroy()
        os.system("admin.py")


def clear():
    fullname.delete(0,END)
    department.delete(0,END)
    age.delete(0,END)
    contact.delete(0,END)
    address.delete(0, END)

def update():
    global my_img
    global main

    if employeeID.get()=="":
        messagebox.showinfo("Error", "Please enter employee ID")
    else:
        root.withdraw()
        main = Toplevel()
        main.geometry("1366x768+60+10")
        main.title("Login")
        main.resizable(0, 0)
        main.iconbitmap('./images/5.ico')

        conn = sqlite3.connect('EmployeeInfo.db')
        c = conn.cursor()
        record_id = employeeID.get()
        c.execute("SELECT*from employees WHERE oid = " + record_id)
        records = c.fetchall()
        global fullname
        global department
        global age
        global var
        global contact
        global address

        # image used as background
        my_img = ImageTk.PhotoImage(Image.open('images/update.png'))
        Label(main, image=my_img).pack()
        # labels created in update admin window
        fullname_lbl = Label(main, text="Full Name", font=('Consolas', 15), bg="white")
        fullname_lbl.place(x=180, y=200)
        department_lbl = Label(main, text="Department", font=('Consolas', 15), bg="white")
        department_lbl.place(x=720, y=200)
        age_lbl = Label(main, text="Age", font=('Consolas', 15), bg="white")
        age_lbl.place(x=180, y=290)
        gender_lbl = Label(main, text="Gender", font=('Consolas', 15), bg="white")
        gender_lbl.place(x=720, y=290)
        contact_lbl = Label(main, text="Contact", font=('Consolas', 15), bg="white")
        contact_lbl.place(x=180, y=380)
        address_lbl = Label(main, text="Address", font=('Consolas', 15), bg="white")
        address_lbl.place(x=720, y=380)

        # entry box created in update admin window
        fullname = Entry(main, width=40, border=0, font=('Consolas', 15))
        fullname.place(x=180, y=230)
        department = Entry(main, width=40, border=0, font=('Consolas', 15))
        department.place(x=720, y=230)
        age = Entry(main, width=40, border=0, font=('Consolas', 15))
        age.place(x=180, y=320)
        var = StringVar()
        r1 = Radiobutton(main, text="Male", value="Male", variable=var, tristatevalue=0, font=('Consolas', 13),
                         bg="white")
        r1.place(x=720, y=320)
        r2 = Radiobutton(main, text="Female", value="Female", variable=var, tristatevalue=0, font=('Consolas', 13),
                         bg="white")
        r2.place(x=800, y=320)
        r3 = Radiobutton(main, text="Other", value="Other", variable=var, tristatevalue=0, font=('Consolas', 13),
                         bg="white")
        r3.place(x=900, y=320)
        contact = Entry(main, width=40, border=0, font=('Consolas', 15))
        contact.place(x=180, y=410)
        address = Entry(main, width=40, border=0, font=('Consolas', 15))
        address.place(x=720, y=410)
        for record in records:
            fullname.insert(0, record[0])
            department.insert(0, record[1])
            age.insert(0, record[2])
            # var.insert(0, record[3])
            contact.insert(0, record[4])
            address.insert(0, record[5])
        update_btn = Button(main, text="UPDATE", font=('Consolas', 15), cursor='hand2',
                            bg="#00bff3", border=0, activebackground="#00bff3", padx=20, pady=10, command=save)
        update_btn.place(x=550, y=630)
        clear_btn = Button(main, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                           bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10, command=clear)
        clear_btn.place(x=715, y=630)


def logout():
    response = messagebox.askyesno('Confirm Logout', 'Are you sure to Logout? ')
    if response==1:
        root.withdraw()
        os.system("main.py")

def refresh():
    root.destroy()
    os.system('admin.py')

def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

#design for admin management window
myimage=ImageTk.PhotoImage(Image.open('./images/adminmanagement.png'))
Label(image=myimage).pack()

# label
id_lbl=Label(root,text="Employee ID",font=('Consolas',13),bg="white")
id_lbl.place(x=120,y=190)
option_lbl=Label(root,text="Administration Option",font=('Consolas',13),bg="white")
option_lbl.place(x=130,y=290)

# entry
employeeID=Entry(root,width=25,border=0,font=('Consolas',13))
employeeID.place(x=60,y=220)
# entryID = employeeID.get()



# buttons
logoutBTN=Button(root,text="LOG OUT",font=('Consolas',13),cursor='hand2',
                  bg="#687afd",border=0,activebackground="#687afd",padx=16,command=logout)
logoutBTN.place(x=1218,y=49)

refreshBTN=Button(root,text="Refresh",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",command=refresh)
refreshBTN.place(x=313,y=178)

searchBTN=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",command=search)
searchBTN.place(x=316,y=218)

addEmpBTN=Button(root,text="ADD EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=90,command=adding)
addEmpBTN.place(x=75,y=330)


updateBTN=Button(root,text="UPDATE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85,command=update)
updateBTN.place(x=65,y=380)
deleteBTN=Button(root,text="DELETE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85,command=delete)
deleteBTN.place(x=65,y=432)

exitBTN =Button(root,text="EXIT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=16,command=Exit)
exitBTN .place(x=185,y=675)

#treeview table created to show information stored in database
conn = sqlite3.connect("EmployeeInfo.db")
c = conn.cursor()
c.execute('SELECT * ,oid from employees')
records = c.fetchall()

my_tree = ttk.Treeview(root)
my_tree['columns'] = ("Sno.","FullName", "Department", "Age","Gender", "Contact","Address")

my_tree.column("#0", width =0, stretch=NO)
my_tree.column("Sno.", anchor=CENTER,width=30)
my_tree.column("FullName", anchor=CENTER,width=150)
my_tree.column("Department", anchor=CENTER,width=120)
my_tree.column("Age", anchor=CENTER,width=40)
my_tree.column("Gender", anchor=CENTER,width=90)
my_tree.column("Contact", anchor=CENTER,width=100)
my_tree.column("Address", anchor=CENTER,width=100)

my_tree.heading("#0", text = "", anchor = CENTER)
my_tree.heading("Sno.", text = "Sno", anchor = CENTER)
my_tree.heading("FullName", text = "FullName", anchor = CENTER)
my_tree.heading("Department", text = "Department", anchor = CENTER)
my_tree.heading("Age", text = "Age", anchor = CENTER)
my_tree.heading("Gender", text = "Gender", anchor = CENTER)
my_tree.heading("Contact", text = "Contact", anchor = CENTER)
my_tree.heading("Address",text = "Address", anchor = CENTER)

my_tree.place(relx=0.307, rely=0.203, width=880, height=550)
count=0
for record in records:
    my_tree.insert(parent='',index='end',iid=count,text="Parent",values=(record[6],record[0],record[1],record[2],record[3],record[4],record[5]))
    count+=1

# Scrollbar for tree view table
scrollbarx = Scrollbar(root, orient=HORIZONTAL)
scrollbary = Scrollbar(root, orient=VERTICAL)
scrollbarx.configure(command=my_tree.xview)
scrollbary.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand= scrollbary.set, xscrollcommand = scrollbarx.set)
scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)


root.mainloop()