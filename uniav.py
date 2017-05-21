from tkinter import Tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os
import hashlib

autoremove = None
autoupdate = None
fyle = None

root = Tk()

#Main frame
mainframe = Frame(root, height=500, width=1000, bg="black", relief=SUNKEN)
mainframe.pack()

#
#Configuring root and Top Window
#
root.wm_title("UNIAV")
root.resizable(0,0)

def scanAFile():
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    global fyle
    fyle = askopenfilename()
    print(fyle)
    with open(fyle, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
            print(hasher.hexdigest())
            filehash = hasher.hexdigest()
            print(filehash)
            if filehash == "1e958e2659e359bea13713061226b681":
                print("Match")
                removeTheFile()

def removeTheFile():
    answer = tkinter.messagebox.askquestion(title="File", message="Do you want to remove this file? It has been found as a threat.")

    if answer == 'yes':
        os.unlink(fyle)
        tkinter.messagebox.showinfo(title="File", message="We have removed the dangerous file.")

def quickScan():
    print("Scanning")
    tkinter.messagebox.showinfo("Scan complete", "The scan has been completed!")

def optionsWindow():
    options = Toplevel()

    autoRemove = Checkbutton(options, text="Automatically remove found threats.", variable=autoremove)
    autoRemove.pack()

    autoUpdate = Checkbutton(options, text="Automatically update definitions while computer is in idle state.", variable=autoupdate)
    autoUpdate.pack()

    options.resizable(0,0)
    options.wm_title("Settings")



title = Label(mainframe, text="Uni Antivirus", fg="white", bg="black")
title.config(font=("Arial", 44))
title.pack(side=TOP)
runQuickScan = Button(mainframe, text="Quick Scan", command=quickScan, fg="white", bg="gray")
runQuickScan.pack(side=LEFT)
runDirScan = Button(mainframe, text="Scan in a certain directory", command=quickScan, fg="white", bg="gray")
runDirScan.pack(side=LEFT)
runOneFileScan = Button(mainframe, text="Scan one file", command=scanAFile, fg="white", bg="gray")
runOneFileScan.pack(side=LEFT)
settingsButton = Button(mainframe, text="Settings", command=optionsWindow, fg="white", bg="gray")
settingsButton.pack(side=LEFT)

root.mainloop()
