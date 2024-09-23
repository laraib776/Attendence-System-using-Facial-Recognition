import tkinter as tk
#import tkMessageBox

# making the window
root1=tk.Tk()
root1.title(' Log_in ')
root1.geometry("500x500")  # set the root11 dimensions
root1.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
root1.resizable(0, 0)
root1.config(background='PeachPuff2')

# defining the str value : assign a StringVar object to the text_variable of a widget
reg_var=tk.StringVar()
pas_var=tk.StringVar()

# Our data for input
dict_1 = {'210201001': '123', '210201002': 'abc', '210201005': 'blah', '210201010': 'wtf',
          '210201006': 'fuck', '210201004': 'D.E.A.D'}

# registration
label1=tk.Label(root1, text=' Registration No. ')
label1.place(x=100, y=50)
label1.config(background='PeachPuff3')

entry_1 = tk.Entry(root1,textvariable = reg_var, font=('calibre',10, 'bold'))
entry_1.place(x=100, y=100)
entry_1.config(background='PeachPuff3')

# password
label2=tk.Label(root1, text=' Password ')
label2.place(x=100, y=150)
label2.config(background='PeachPuff3')

bad_pass = tk.Label(root1, text="Incorrect Username or Password")

entry_2 = tk.Entry(root1,textvariable = pas_var,show="*", font=('calibre',10, 'bold'))
entry_2.place(x=100, y=200)
entry_2.config(background='PeachPuff3')

# function for information
def display(name):
    if name == "210201001":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='PeachPuff2')

        lbl1 = tk.Label(win, text='Name :')
        lbl1.config(background='PeachPuff2')
        a = tk.Label(win, text='Laraib Khalid')
        a.config(background='PeachPuff2')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        lbl2.config(background='PeachPuff2')
        b = tk.Label(win, text='210201001')
        b.config(background='PeachPuff2')
        lbl3 = tk.Label(win, text='Department :')
        lbl3.config(background='PeachPuff2')
        c = tk.Label(win, text='CS_02')
        c.config(background='PeachPuff2')
        lbl4 = tk.Label(win, text='Phone Number :')
        lbl4.config(background='PeachPuff2')
        d = tk.Label(win, text='0300-5289-8401')
        d.config(background='PeachPuff2')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.Button(win, text="  Exit  ", command=win.destroy)
        btn.place(x=200, y=300)
        btn.config(background='PeachPuff1')
        win.mainloop()

    elif name == "210201004":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='navajo white')

        lbl1 = tk.Label(win, text='Name :')
        a = tk.Label(win, text='Laiba Qayoom')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        b = tk.Label(win, text='210201005')
        lbl3 = tk.Label(win, text='Department :')
        c = tk.Label(win, text='CS_02')
        lbl4 = tk.Label(win, text='Phone Number :')
        d = tk.Label(win, text='0301-5228-8482')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.Button(win, text="  Exit  ", fg='gray', command=win.destroy)
        btn.place(x=200, y=300)
        win.mainloop()

    elif name == "210201006":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='navajo white')

        lbl1 = tk.Label(win, text='Name :')
        a = tk.Label(win, text='Laiba Ehsan')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        b = tk.Label(win, text='210201006')
        lbl3 = tk.Label(win, text='Department :')
        c = tk.Label(win, text='CS_02')
        lbl4 = tk.tk.Label(win, text='Phone Number :')
        d = tk.Label(win, text='0304-5678-9072')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.Button(win, text="  Exit  ", fg='gray', command=win.destroy)
        btn.place(x=200, y=300)
        win.mainloop()

    elif name == "210201002":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='navajo white')

        lbl1 = tk.Label(win, text='Name :')
        a = tk.Label(win, text='Sundas')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        b = tk.Label(win, text='210201002')
        lbl3 = tk.Label(win, text='Department :')
        c = tk.Label(win, text='CS_02')
        lbl4 = tk.Label(win, text='Phone Number :')
        d = tk.Label(win, text='0304-5888-9882')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.Button(win, text="  Exit  ", fg='gray', command=win.destroy)
        btn.place(x=200, y=300)
        win.mainloop()

    elif name == "2102010010":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='navajo white')

        lbl1 = tk.Label(win, text='Name :')
        a = tk.Label(win, text='Zoya')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        b = tk.tk.tk.Label(win, text='210201010')
        lbl3 = tk.tk.Label(win, text='Department :')
        c = tk.Label(win, text='CS_02')
        lbl4 = tk.Label(win, text='Phone Number :')
        d = tk.Label(win, text='0304-7678-9992')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.tk.Button(win, text="  Exit  ", fg='gray', command=win.destroy)
        btn.place(x=200, y=300)
        win.mainloop()

    elif name == "210201005":
        win = tk.Tk()
        win.title('__Personal Information__')

        win.geometry("500x500")  # set the root1 dimensions
        win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
        win.resizable(0, 0)  # makes the root1 window fixed in size.
        win.config(background='navajo white')

        lbl1 = tk.Label(win, text='Name :')
        a = tk.Label(win, text='Zainab')
        lbl2 = tk.Label(win, text='Registrarion Number :')
        b = tk.Label(win, text='210201005')
        lbl3 = tk.Label(win, text='Department :')
        c = tk.Label(win, text='CS_02')
        lbl4 = tk.Label(win, text='Phone Number :')
        d = tk.Label(win, text='0304-0078-9070')
        lbl1.place(x=100, y=50)
        lbl2.place(x=100, y=100)
        lbl3.place(x=100, y=150)
        lbl4.place(x=100, y=200)
        a.place(x=200, y=50)
        b.place(x=250, y=100)
        c.place(x=200, y=150)
        d.place(x=200, y=200)

        btn = tk.Button(win, text="  Exit  ", fg='gray', command=win.destroy)
        btn.place(x=200, y=300)
        win.mainloop()

# validate data input or not
def check_login():
    requested_user = reg_var.get()
    try:
        if dict_1[requested_user] == pas_var.get():
            display(requested_user)
        else:
            bad_pass.grid(row=2, column=1)
    except KeyError:
        bad_pass.grid(row=2, column=1)

# button_for submission
submit = tk.Button(root1, text="  Submit  ", command=check_login)
submit.place(x=100, y=300)
submit.config(background='PeachPuff3')

# button to exit
cancelButton = tk.Button(root1, text="Cancel", command=quit)
cancelButton.place(x=200,y=300)
cancelButton.config(background='PeachPuff3')

root1.mainloop()
