__author__ = 'colt'

from tkinter import *
from screen_now_playing import NowPlayingScreen
from screen_music_library import MusicLibraryScreen


class MainScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.main_container = Frame(parent, background="bisque")
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)
        self.main_navigation = Frame(self.main_container, background="green")
        self.main_navigation.pack(side=LEFT, fill=Y, expand=False)
        self.details_frame = Frame(self.main_container, background="yellow")
        self.details_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        self.details_frame.grid_rowconfigure(0, weight=1)
        self.details_frame.grid_columnconfigure(0, weight=1)

        nowplayingputton = Button(self.main_navigation, text="Now Playing", command=self.display_audio_playing)
        nowplayingputton.pack(side=TOP)
        playlistbutton = Button(self.main_navigation, text="Playlists", command=self.display_playlist)
        playlistbutton.pack(side=TOP)
        browselibrarybutton = Button(self.main_navigation, text="Browse Library", command=self.browse_library)
        browselibrarybutton.pack(side=TOP)
        settingsbutton = Button(self.main_navigation, text="Settings")
        settingsbutton.pack(side=BOTTOM)

        self.display_audio_playing()

    def show_frame(self, Screen):
        _list = self.details_frame.winfo_children()
        for i in _list:
            i.destroy()
        Screen(self.details_frame)

    def display_audio_playing(self):
        self.show_frame(NowPlayingScreen)

    def display_playlist(self):
        print("display play list")

    def browse_library(self):
        self.show_frame(MusicLibraryScreen)

