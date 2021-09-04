from tkinter import *
from PIL import Image,ImageTk
import os
import addemployee
import sqlite3
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.geometry("1366x768+60+10")
root.title("Login")
root.resizable(0, 0)

# creating database
# conn = sqlite3.connect("EmployeeInfo.db")
# c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#         FullName text,
#         Department text,
#         Age integer,
#         Gender text,
#        Contact integer,
#          Address text
#  )""")
# conn.commit()
# conn.close()

#function
def logout():
    root.withdraw()
    os.system("main.py")
def refresh():
    root.destroy()
    os.system('employee.py')
def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

def adding():
    root.withdraw()

    addemployee.add()



myimage=ImageTk.PhotoImage(Image.open('./images/empmanagement.png'))
Label(image=myimage).pack()

# label
id_lbl=Label(root,text="Employee ID",font=('Consolas',13),bg="white")
id_lbl.place(x=120,y=190)
option_lbl=Label(root,text="Employee Option",font=('Consolas',13),bg="white")
option_lbl.place(x=155,y=290)

# entry
employeeID=Entry(root,width=25,border=0,font=('Consolas',13))
employeeID.place(x=60,y=220)
# entryID = employeeID.get()

# buttons
logoutBTN=Button(root,text="LOG OUT",font=('Consolas',13),cursor='hand2',
                  bg="#687afd",border=0,activebackground="#687afd",padx=16,command=logout)
logoutBTN.place(x=1218,y=49)

searchBTN=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3")
searchBTN.place(x=316,y=218)

addEmpBTN=Button(root,text="ADD EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=90,command=adding)
addEmpBTN.place(x=75,y=330)

updateBTN=Button(root,text="UPDATE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
updateBTN.place(x=65,y=380)
refreshBTN=Button(root,text="Refresh",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",command=refresh)
refreshBTN.place(x=313,y=178)

exitBTN =Button(root,text="EXIT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=16,command=Exit)
exitBTN .place(x=185,y=675)

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

# Scrollbar
scrollbarx = Scrollbar(root, orient=HORIZONTAL)
scrollbary = Scrollbar(root, orient=VERTICAL)
scrollbarx.configure(command=my_tree.xview)
scrollbary.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand= scrollbary.set, xscrollcommand = scrollbarx.set)
scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

root.mainloop()