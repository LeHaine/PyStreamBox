__author__ = 'colt'

from screen_main import MainScreen
from tkinter import *
from mpd import MPDClient

class Application:
    def __init__(self, master):
        self.master = master
        self.connect_mpd()
        self.create_screens()
        self.apply_fullscreen()

    def connect_mpd(self):
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.idletimeout = None
    """ self.client.connect("localhost", 6600)
        print(self.client.mpd_version)
        print(self.client.find("any", "house"))
        self.client.close()
        self.client.disconnect() """

    def create_screens(self):
        MainScreen(self.master)

    def apply_fullscreen(self):
      #  self.master.attributes('-zoomed', True)
        self.fullscreen_state = False
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.fullscreen_state = not self.fullscreen_state
        self.master.attributes("-fullscreen", self.fullscreen_state)
        return "break"

    def end_fullscreen(self, event=None):
        self.fullscreen_state = False
        self.master.attributes("-fullscreen", False)
        return "break"


if __name__ == "__main__":
    root = Tk()
    root.title("PyStreamBox")
    root.geometry("320x240+300+300")
    application = Application(root)
    root.mainloop()



