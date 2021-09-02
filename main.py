from tkinter import *

root = Tk()
root.lift()
root.geometry("1366x768+60+10")
root.title("Employee Management System")
root.resizable(0, 0)



label1 = Label(root)
label1.place(x=0, y=0, width=1366, height=768)


button1 = Button(root,bg='white',fg='white',activebackground="white",relief="flat",overrelief="flat",borderwidth="0",
                 cursor='hand2')
button1.place(x=430,y=330, width=146, height=90)
Label(root,text='EMPLOYEE',bg='white',font=('Consolas',15)).place(x=455,y=410)


button2 = Button(root,bg='white',fg='white',activebackground="white",relief="flat",overrelief="flat",borderwidth="0",
                 cursor='hand2')
button2.place(x=774,y=330, width=146, height=100)
Label(root,text='ADMIN',bg='white',font=('Consolas',15)).place(x=815,y=410)


root.mainloop()
