from http.server import executable
import tkinter as tk
from tkinter import filedialog, Text
import os
import os, sys, subprocess

root = tk.Tk()
apps = [ ]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("executables","*.app"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApp():
    for app in apps:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, app])

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApp)
openFile.pack()
runApps.pack()

root.mainloop()

