import tkinter as tk

import Pmw as Pmw

import services as db
from tkinter import messagebox
import search as sc
import passwordgenerator as pg

currentUser = None

root = tk.Tk()
root.geometry("540x600")
root.title("Password Manager")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# copying mech
def gtc(dtxt):
    print('value here is' , dtxt)
    root.clipboard_clear()
    root.clipboard_append(dtxt)



def showFrame(frame):
    frame.tkraise()
    masterusnm_field.delete(0, tk.END)
    masterPassword_field.delete(0, tk.END)


# ADD PAGE FRAME ########################################
addPageFrame = tk.Frame(root)
showPasswordsFrame = tk.Frame(root, bg='orange')

lb1 = tk.Label(addPageFrame, text="Site", width=4, font=("arial", 12))
lb1.place(x=20, y=120)
title = tk.Entry(addPageFrame)
title.place(x=200, y=120)

lb2 = tk.Label(addPageFrame, text="Username", width=9, font=("arial", 12))
lb2.place(x=20, y=160)
email = tk.Entry(addPageFrame)
email.place(x=200, y=160)

lb3 = tk.Label(addPageFrame, text="Password", width=10, font=("arial", 12))
lb3.place(x=15, y=200)
passwordField = tk.Entry(addPageFrame, show='*')
passwordField.place(x=200, y=200)


def toggle_password():
    if passwordField.cget('show') == '':
        passwordField.config(show='*')
        repassword.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        passwordField.config(show='')
        repassword.config(show='')
        toggle_btn.config(text='Hide Password')


toggle_btn = tk.Button(addPageFrame, text='Show Password', width=20, command=toggle_password)
toggle_btn.place(x=350, y=240)

lb4 = tk.Label(addPageFrame, text="Confirm Password", width=15, font=("arial", 12))
lb4.place(x=20, y=240)
repassword = tk.Entry(addPageFrame, show='*')
repassword.place(x=200, y=240)


###LOGIN FRAME
loginFrame = tk.Frame(root, bg='#D1CBC1')
tk.Label(loginFrame, text='Password Manager', bg='#D1CBC1', width=25, font=('arial', 20, 'bold')).place(x=30, y=80)
tk.Label(loginFrame, text='Username', bg='#D1CBC1', width=25, font=('arial', 12, 'bold')).place(x=-25, y=150)
tk.Label(loginFrame, text='Password', bg='#D1CBC1', width=25, font=('arial', 12, 'bold')).place(x=-25, y=173)
masterusnm_field = tk.Entry(loginFrame, show='', width=25, borderwidth=5)
masterusnm_field.place(x=150, y=150)
masterPassword_field = tk.Entry(loginFrame, show='*', width=25, borderwidth=5)
masterPassword_field.place(x=150, y=170)


def save():
    if passwordField.get() == repassword.get():
        entry = {
            'site': title.get(),
            'username': email.get(),
            'password': passwordField.get()
        }
        db.addPassword(entry, currentUser)
        title.delete(0, tk.END)
        email.delete(0, tk.END)
        passwordField.delete(0, tk.END)
        repassword.delete(0, tk.END)
    else:
        tk.messagebox.showinfo("Alert", "Password doesn't match!!")


def generatePassword():
    newPassword = pg.generatePassword()

    passwordField.delete(0, tk.END)
    repassword.delete(0, tk.END)

    passwordField.insert(0, newPassword)
    repassword.insert(0, newPassword)


tk.Button(addPageFrame, text="Generate Password", width=20, command=generatePassword).place(x=350, y=200)

tk.Button(addPageFrame, text="Save", width=10, command=save).place(x=200, y=280)

def deletePassword(id):
    ## takes the index
    print()
    db.deletePassword(id, currentUser)
    showPasswords()

def showPasswords():
    # SHOW PASSWORDS FRAME ################################  deletePassword(pw[0])
    for widget in showPasswordsFrame.winfo_children():
        widget.destroy()
    passwords = db.getPasswords(currentUser)


    site_title = tk.Label(showPasswordsFrame, text='Site', width=10, bg='orange', font=("arial", 15))
    site_title.place(x=10, y= 30)

    username_title = tk.Label(showPasswordsFrame, text='Username', width=10, bg='orange', font=("arial", 15))
    username_title.place(x=150, y= 30 )

    password_title = tk.Label(showPasswordsFrame, text='Password', width=12, bg='orange', font=("arial", 15))
    password_title.place(x=300, y=30 )

    for index, pw in enumerate(passwords):
        print(pw)
        l1 = tk.Label(showPasswordsFrame, text=pw[1], width=10, bg='orange', font=("arial", 12))
        l1.place(x=10, y=30 * (index) + 75)
        temp_btn1 = tk.Button(showPasswordsFrame , name = ('copy' + str(index)), text='Copy', bg='orange')
        temp_btn1.pack()
        temp_btn1.bind('<Button>' , lambda x: gtc( passwords[  int((str(x.widget).split(".")[-1])[-1])  ][3]) )
        temp_btn1.place(x=420, y=30 * (index) + 75)


        temp_btn2 = tk.Button(showPasswordsFrame, name = str(pw[0]),text='Delete', bg='orange')
        temp_btn2.pack()
        temp_btn2.bind('<Button>', lambda x: deletePassword(str(x.widget).split(".")[-1]))
        temp_btn2.place(x=480, y=30 * (index) + 75)                                                                                   
        

        l2 = tk.Label(showPasswordsFrame, text=pw[2], width=10, bg='orange', font=("arial", 12))
        l2.place(x=150, y=30 * (index) + 75)

        l3 = tk.Label(showPasswordsFrame, text=pw[3], width=12, bg='orange', font=("arial", 12))
        l3.place(x=300, y=30 * (index) + 75)

    tk.Button(showPasswordsFrame, text="Back", width=25, command=lambda: showFrame(addPageFrame)).place(x=160, y=400)

    showFrame(showPasswordsFrame)


tk.Button(showPasswordsFrame, text="Back", width=25, command=lambda: showFrame(addPageFrame)).place(x=160, y=340)
tk.Button(addPageFrame, text="Show Saved Passwords", width=25, command=showPasswords).place(x=200, y=340)


#############################################

###############################################

# LOGINPAGE ###################################


def register():
    window = tk.Tk()
    window.title('New Account')

    def toggle_passwordm1():
        if master_password_field.cget('show') == '':
            master_password_field.config(show='*')
            cnfmpass.config(show='*')
            toggle_btnm2.config(text='Show Password')
        else:
            master_password_field.config(show='')
            cnfmpass.config(show='')
            toggle_btnm2.config(text='Hide Password')

    def generatePassword1():
        newPassword = pg.generatePassword()

        master_password_field.delete(0, tk.END)
        cnfmpass.delete(0, tk.END)

        master_password_field.insert(0, newPassword)
        cnfmpass.insert(0, newPassword)

    tk.Button(window, text="Generate Password", borderwidth=3, width=15, command=generatePassword1).place(x=370, y=88)
    toggle_btnm2 = tk.Button(window, borderwidth=3, text='Show Password', width=15, command=toggle_passwordm1)
    toggle_btnm2.place(x=370, y=138)

    tk.Label(window, text='Create Account', width=25, font=('arial', 20, 'bold')).place(x=0, y=0)
    tk.Label(window, text='Username', width=25, font=('arial', 12, 'bold')).place(x=10, y=40)
    tk.Label(window, text='Password', width=25, font=('arial', 12, 'bold')).place(x=10, y=90)
    tk.Label(window, text='Confirm', width=25, font=('arial', 12, 'bold')).place(x=10, y=140)

    master_usnm_field = tk.Entry(window, show='', width=25, borderwidth=5)
    master_usnm_field.place(x=200, y=40)
    master_password_field = tk.Entry(window, show='*', width=25, borderwidth=5)
    master_password_field.place(x=200, y=90)
    cnfmpass = tk.Entry(window, show='*', width=25, borderwidth=5)
    cnfmpass.place(x=200, y=140)

    def createacc():
        masterusnm = master_usnm_field.get()
        masterpassword = master_password_field.get()

        entry = {
                'username': masterusnm,
                'password': masterpassword
            }
        db.createAccount(entry)
        master_usnm_field.delete(0, tk.END)
        master_password_field.delete(0, tk.END)
        cnfmpass.delete(0, tk.END)
        messagebox.showinfo('Info', 'Account Created')
        window.destroy()

    tk.Button(window, text="Create", bg='deep sky blue', borderwidth=2, width=15, command=createacc).place(x=200, y=180)
    window.geometry('490x220')
    window.mainloop()


def login():
    enteredPassword = masterPassword_field.get()
    enteredUsername = masterusnm_field.get()

    entry = {
        'username' : enteredUsername,
        'password' : enteredPassword
    }
    if(db.login(entry)):
        global currentUser
        currentUser = enteredUsername
        showFrame(addPageFrame)
    else:
        messagebox.showerror('Error', 'Invalid credentials')

def toggle_passwordm():
    if masterPassword_field.cget('show') == '':
        masterPassword_field.config(show='*')
        toggle_btnm.config(text='Show Password')
    else:
        masterPassword_field.config(show='')
        toggle_btnm.config(text='Hide Password')


toggle_btnm = tk.Button(loginFrame, borderwidth=3, bg='#918D86', text='Show Password', width=15,
                        command=toggle_passwordm)
toggle_btnm.place(x=330, y=170)
tk.Button(loginFrame, text="Login", bg='#918D86', borderwidth=2, width=15, command=login).place(x=173, y=240)
tk.Button(loginFrame, text="Register", bg='#918D86', borderwidth=2, width=15, command=register).place(x=173, y=270)

######## hover info

Pmw.initialise(root)  # initializing it in the root window
b = tk.Label(loginFrame, text='Info', bg='blue', width=5)
b.place(x=455, y=0)
tooltip_1 = Pmw.Balloon(loginFrame)  # Calling the tooltip
tooltip_1.bind(b, 'Password generator\nChange the text')  # binding it and assigning a text to it

##################################################
for frame in (loginFrame, addPageFrame, showPasswordsFrame):
    frame.grid(row=0, column=0, sticky='nsew')

showFrame(loginFrame)

addPageFrame.mainloop()
