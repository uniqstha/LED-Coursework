from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter import messagebox
root=Tk()
root.geometry("1366x768+60+10")
root.title("Login")
root.resizable(0, 0)

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
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=90)
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

root.mainloop()