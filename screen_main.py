__author__ = 'colt'

from tkinter import *
from PIL import Image, ImageTk
from screen_now_playing import NowPlayingScreen
from screen_music_library import MusicLibraryScreen
import os


class MainScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.current_button_selected = None
        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)
        self.main_navigation = Frame(self.main_container)
        self.main_navigation.pack(side=LEFT, fill=Y, expand=False)
        self.details_frame = Frame(self.main_container)
        self.details_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.resources_folder_path = os.path.dirname(__file__)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_now_playing.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.nowplaying_icon = ImageTk.PhotoImage(resized)
        self.nowplaying_button = Button(self.main_navigation, image=self.nowplaying_icon, command=self.display_audio_playing)
        self.nowplaying_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_list.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.playlist_icon = ImageTk.PhotoImage(resized)
        self.playlist_button = Button(self.main_navigation, image=self.playlist_icon, command=self.display_playlist)
        self.playlist_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_library.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.browselibrary_icon = ImageTk.PhotoImage(resized)
        self.browselibrary_button = Button(self.main_navigation, image=self.browselibrary_icon, command=self.browse_library)
        self.browselibrary_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/settings.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.settings_icon = ImageTk.PhotoImage(resized)
        self.settings_button = Button(self.main_navigation, image=self.settings_icon)
        self.settings_button.pack(side=BOTTOM)

        self.browse_library()

    def show_frame(self, screen):
        _list = self.details_frame.winfo_children()
        for i in _list:
            i.destroy()
        screen(self.details_frame)

    def disable_button(self, button):
        if self.current_button_selected is not None:
            self.current_button_selected["state"] = NORMAL
        self.current_button_selected = button
        self.current_button_selected["state"] = DISABLED

    def display_audio_playing(self):
        self.disable_button(self.nowplaying_button)
        self.show_frame(NowPlayingScreen)

    def display_playlist(self):
        self.disable_button(self.playlist_button)
        print("display play list")

    def browse_library(self):
        self.disable_button(self.browselibrary_button)
        self.show_frame(MusicLibraryScreen)

