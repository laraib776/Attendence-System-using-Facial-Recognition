import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import *
from tkinter import ttk
from project import files, files1
import pandas as pd
import customtkinter

root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
root.geometry("800x800") # set the root dimensions

values= ['01-04-2023','01-07-2023 CS', '01-07-2023 EE', '01-08-2023 EE',
         '01-08-2023 EE', '01-09-2023 CS', '01-09-2023 EE']

x=files.pop()
x1= files1.pop()

values.append(x)
values.append(x1)

def check(e):
   v= entry_1.get()
   if v=='':
      data= values
   else:
      data=[]
      for item in values:
         if v.lower() in item.lower():
            data.append(item)
   update(data)
def update(data):
   # Clear the Combobox
   menu.delete(0, END)
   # Add values to the combobox
   for value in data:
      menu.insert(END,value)
      

frame_1 = customtkinter.CTkFrame(root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


frame_2 = customtkinter.CTkFrame(frame_1)
frame_2.pack(pady=50, padx=60, fill="both", expand=True)
frame_2.place(height=400, width=600,  rely=0.15, relx=0.50)

label_1 = customtkinter.CTkLabel(frame_1, text='Check Attendance', justify=tk.LEFT, font = ('Times New Roman', 50))
label_1.pack(pady=10, padx=10)

label_1 = customtkinter.CTkLabel(frame_2, text='Files', font = ('Times New Roman', 35))
label_1.pack(pady=10, padx=10)


file_frame = tk.LabelFrame(frame_1, text="Open File",  background="#808080")
file_frame.place(height=400, width=600, rely=0.15, relx=0.01)


button1 = customtkinter.CTkButton(frame_2, text="Browse A File", command=lambda: File_dialog())
button1.pack(pady=30, padx=20)
button1.place(rely=0.50, relx=0.10)


button2= customtkinter.CTkButton(frame_2, text="Load File",command=lambda: Load_excel_data())
button2.pack(pady=30, padx=20)
button2.place(rely=0.30, relx=0.10)


label_file= ttk.Label(frame_2, text="No File Selected",  background="#808080")
label_file.place(rely=0.80, relx=0.10)


entry_1 = customtkinter.CTkEntry(frame_2, placeholder_text="File Name")
entry_1.pack(pady=10, padx=10)
entry_1.bind('<KeyRelease>',check)
entry_1.place(rely=0.68, relx=0.55)

menu= Listbox(frame_2, height=10,  background="#808080")
menu.place(rely=0.18, relx=0.55)

def selected_item():
    i = menu.curselection()
    x = menu.get(i)
    x1 = x + ".csv"
    filename = x1
    label_file["text"] = filename
    file_path = label_file["text"]
    excel_filename = r"{}".format(file_path)
    if excel_filename[-4:] == ".csv":
        df = pd.read_csv(excel_filename)
    clear_data()
    
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. 
    return None


btn= customtkinter.CTkButton(frame_2, text='Print Selected', command=selected_item)
btn.pack(pady=30, padx=20)
btn.place(rely=0.80, relx=0.55)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview", background='#D3D3D3', foreground = 'black', 
                rowheight= 25, fieldbackgrounf = '#D3D3D3')
style.map('Treeview', background= [('selected', 'blue')])

tv1 = ttk.Treeview(file_frame, style = 'Treeview')
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(file_frame, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(file_frame, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("csv files", ".csv"),("All Files", "*.*")))
    label_file["text"] = filename
    return None
def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. 
    return None
def clear_data():
    tv1.delete(*tv1.get_children())
    return None

update(values)

root.mainloop()