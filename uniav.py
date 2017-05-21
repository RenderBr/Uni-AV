from tkinter import Tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os
import hashlib
import readhash
import time
import shutil


# This is a fork of Kicomav, an antivirus made in Python.
# New Author: RenderBr

#changing compass directions bcuz it's annoying
right = E
top = N
left = W
bottom = S

autoremove = None
autoupdate = None
languageList = []
languageList.append('English')
languageList.append('Chinese')
languageList.append('Spanish')
selectedLanguage = languageList[0]
fyle = None

root = Tk()

#Main frame
mainframe = Frame(root, height=500, width=1000, bg="black", relief=SUNKEN)
mainframe.pack()

#
#Configuring root and Top Window
#
root.wm_title("Uni Antivirus")
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
                print("You are infected!")
                removeTheFile()

def removeTheFile():
    answer = tkinter.messagebox.askquestion(title="A threat has been found!", message="Do you want to remove the threat?")

    if answer == 'yes':
        shutil.rmtree(fyle)
        tkinter.messagebox.showinfo(title="The threat has been removed!", message="We have removed the threat successfully")

def quickScan():
    print("Scanning")
    tkinter.messagebox.showinfo("Scan complete", "The scan has been completed!")

def optionsWindow():
    options = Toplevel()

    autoRemove = Checkbutton(options, text="Automatically remove found threats.", variable=autoremove)
    autoRemove.pack()

    autoUpdate = Checkbutton(options, text="Automatically update definitions while computer is in idle state.", variable=autoupdate)
    autoUpdate.pack()

    language = OptionMenu(options, selectedLanguage, *languageList)
    language.pack()

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
