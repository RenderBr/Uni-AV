import hashlib
from tkinter import Tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os


def scanAFile():
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    fyle = askopenfilename()
    with open(fyle, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
            print(hasher.hexdigest())
            filehash = hasher.hexdigest()
            print(filehash)
            if filehash == "bf18544d73a5e44da96b09f833f37e3a":
                print("You are infected!")

