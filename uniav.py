from tkinter import *
import tkinter.messagebox

# This is a fork of Kicomav, an antivirus made in Python.
# New Author: RenderBr

#changing compass directions bcuz it's annoying
right = E
top = N
left = W
bottom = S

autoremove = 0

root = Tk()

#Main frame
mainframe = Frame(root, height=500, bg="black", relief=SUNKEN)
mainframe.pack()

#Configuring root and Top Window
root.wm_title("Uni Antivirus")
root.resizable(0,0)

def quickScan():
    print("Scanning")
    tkinter.messagebox.showinfo("Scan complete", "The scan has been completed!")

def optionsWindow():
    options = Toplevel()

    autoRemove = Checkbutton(options, text="Automatically remove found threats.", variable=autoremove)
    autoRemove.pack()

    options.resizable(0,0)
    options.wm_title("Settings")



title = Label(mainframe, text="Uni Antivirus", fg="white", bg="black")
title.config(font=("Arial", 44))
title.pack(side=TOP)
runQuickScan = Button(mainframe, text="Quick Scan", command=quickScan, fg="white", bg="gray")
runQuickScan.pack(side=LEFT)
runDirScan = Button(mainframe, text="Scan in a certain directory", command=quickScan, fg="white", bg="gray")
runDirScan.pack(side=LEFT)
settingsButton = Button(mainframe, text="Settings", command=optionsWindow, fg="white", bg="gray")
settingsButton.pack(side=LEFT)





root.mainloop()