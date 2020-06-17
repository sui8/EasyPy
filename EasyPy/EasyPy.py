import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def pError(Reason):
	print("[EasyPy] Error: " + Reason)

def MessageBox(ver, title, message):

    root = tk.Tk()
    root.withdraw()

    ver.lower()

    if ver == "info":
        messagebox.showinfo(title, message)

    elif ver == "warning":
        messagebox.showwarning(title, message)

    elif ver == "error":
        messagebox.showerror(title, message)

    elif ver == "askquestion":
        messagebox.askquestion(title, message)

    elif ver == "askcancel":
        messagebox.askcancel(title, message)

    elif ver == "askyesno":
        messagebox.askyesno(title, message)

    elif ver == "askretrycancel":
        messagebox.askretrycancel(title, message)

    else:
        pError("MessageBox")

def Dialog(title, message):

    try:
        simpledialog.askstring(title, message)

    except:
        pError("Dialog")