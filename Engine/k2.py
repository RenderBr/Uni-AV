from tkinter import *
import tkinter.messagebox

# This is a fork of Kicomav, an antivirus made in Python.
# New Author: RenderBr



#changing compass directions bcuz it's annoying
right = E
up = N
left = W
down = S

root = Tk()



#Configuring root
root.wm_title("Alpha Antivirus")

def quickScan():
    print("Scanning")
    tkinter.messagebox.showinfo("Scan complete", "The scan has been completed!")

runScan = Button(root, text="Quick Scan", command=quickScan)
runScan.pack(side=TOP)





root.mainloop()