import tkinter as tk
from tkinter import *
from PIL import ImageTk
import sqlite3
import hashlib
import tkinter.messagebox

#bg_col= "#001B1A"
bg_col="white"

    

#********************************************************************************************************************frame1
def load_frame1():
    def signin():
        username=user.get()
        #password=pwd.get()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        if len(c.execute("select username from user where username = ?",(username,)).fetchall())>0:
            #password1 = hashlib.sha256(password.encode()).hexdigest()
            query = c.execute("select username,password from user where (username)=(?)",(username,)).fetchone()
            #if password1 == query[1]:
                #tkinter.messagebox.showinfo
                #("authentification succusfull")
                #root.destroy()
            #else:
                #tkinter.messagebox.showerror("Please verify you password!")
        else:
            tkinter.messagebox.showerror("User does not exist! Please register first!. ")
    
    
    
    
    frame1.pack_propagate(False)

    #frame1 widgets
    recept = ImageTk.PhotoImage(file="res/TchatY.png")
    recept_widget = tk.Label(frame1, image=recept, bg=bg_col)
    recept_widget.image = recept
    recept_widget.pack()

    #frame1 text
    tk.Label(
        frame1,
        text="Welcome To Be Secure",
        bg=bg_col,
        fg="white",
        font=("TkMenuFont", 14)
        ).pack()

    #frame1 username
         
    def on_enter(e):
        name=user.get()
        if name=='Username':
            user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user = tk.Entry(frame1,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    user.place(x=165,y=330)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #frame1 password
    def on_enter(e):
        mdp=password.get()
        if mdp=='Password':
            password.delete(0, 'end')

    def on_leave(e):
        mdp=password.get()
        if mdp=='':
            password.insert(0,'Password')
    password = tk.Entry(frame1,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    password.place(x=165,y=360)
    password.insert(0,'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    #frame1 button SignIn
    inbut=tk.Button(
            frame1,
            text="Sign In",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="black",
            activeforeground="#badee2",
            command=signin
            )
    inbut.place(x=235,y=400)

    #frame1 button SignUp
    outbut=tk.Button(
            frame1,
            text="Sign Up",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="white",
            activeforeground="#badee2",
            command=lambda:load_frame2()
            )
    outbut.place(x=230,y=450)

#********************************************************************************************************************frame2
def load_frame2():
    #frame1.pack_propagate(False)
    #frame2 widgets
    recept = ImageTk.PhotoImage(file="res/TchatY.png")
    recept_widget = tk.Label(frame2, image=recept, bg=bg_col)
    recept_widget.image = recept
    recept_widget.pack()
        
    #frame2 text
    tk.Label(
        frame2,
        text="Welcome To Be Secure",
        bg=bg_col,
        fg="white",
        font=("TkMenuFont", 14)
        ).pack()

    #frame2 firstname        
    def on_enter(e):
        fn=fname.get()
        if fn=='First Name':
            fname.delete(0, 'end')

    def on_leave(e):
        fn=fname.get()
        if fn=='':
            fname.insert(0,'First Name')
    fname = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    fname.place(x=35,y=300)
    fname.insert(0,'First Name')
    fname.bind('<FocusIn>', on_enter)
    fname.bind('<FocusOut>', on_leave)

    #frame2 lastname        
    def on_enter(e):
        ln=lname.get()
        if ln=='Last Name':
            lname.delete(0, 'end')

    def on_leave(e):
        ln=lname.get()
        if ln=='':
            lname.insert(0,'Last Name')
    lname = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    lname.place(x=35,y=330)
    lname.insert(0,'Last Name')
    lname.bind('<FocusIn>', on_enter)
    lname.bind('<FocusOut>', on_leave)

    #frame2 cardnumber        
    def on_enter(e):
        cn=cardn.get()
        if cn=='Card Number':
            cardn.delete(0, 'end')

    def on_leave(e):
        cn=cardn.get()
        if cn=='':
            cardn.insert(0,'Card Number')
    cardn = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    cardn.place(x=35,y=360)
    cardn.insert(0,'Card Number')
    cardn.bind('<FocusIn>', on_enter)
    cardn.bind('<FocusOut>', on_leave)

    #frame2 username        
    def on_enter(e):
        name=user.get()
        if name=='Username':
            user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    user.place(x=35,y=390)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #frame1 password
    def on_enter(e):
        mdp=password.get()
        if mdp=='Password':
            password.delete(0, 'end')

    def on_leave(e):
        mdp=password.get()
        if mdp=='':
            password.insert(0,'Password')
    password = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    password.place(x=135,y=390)
    password.insert(0,'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    #frame1 Retrypassword
    def on_enter(e):
        rmdp=password.get()
        if rmdp=='Retry Password':
            rpassword.delete(0, 'end')

    def on_leave(e):
        rmdp=rpassword.get()
        if rmdp=='':
            rpassword.insert(0,'Retry Password')
    rpassword = tk.Entry(frame2,width=25,fg='white',border=0,bg="black",font=('Microsoft YaHei UI Light',11))
    rpassword.place(x=35,y=420)
    rpassword.insert(0,'Retry Password')
    rpassword.bind('<FocusIn>', on_enter)
    rpassword.bind('<FocusOut>', on_leave)

    #frame2 button Submit
    subut=tk.Button(
            frame2,
            text="Submit",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="black",
            activeforeground="#badee2",
            #command=Control
            )
    subut.place(x=35,y=450)

    #frame2 button Sign In
    inbut=tk.Button(
            frame2,
            text="Sign In",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="black",
            activeforeground="#badee2",
            #command=Control
            )
    inbut.place(x=35,y=490)

# initiallize app
root = tk.Tk()
root.title("TchatY")
#root.eval("tk::PlaceWindow . center")
x=root.winfo_screenwidth()//4
y=int(root.winfo_screenheight()*0.1)
root.geometry('600x800+' + str(x) + '+' + str(y))

#create a frame widget
frame1 = tk.Frame(root, width=600, height=800, bg=bg_col )
frame2 = tk.Frame(root, bg=bg_col )
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()

