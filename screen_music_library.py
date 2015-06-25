__author__ = 'colt'

from tkinter import *

class MusicLibraryScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.main_container = Frame(parent, background="orange")
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)
        Button(self.main_container, text="1").pack(side=TOP)
        Button(self.main_container, text="2").pack(side=TOP)
        Button(self.main_container, text="3").pack(side=TOP)