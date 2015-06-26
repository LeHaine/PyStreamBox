__author__ = 'colt'

from tkinter import *
from PIL import Image, ImageTk
import os

class MusicLibraryScreen:

    def __init__(self, parent):
        self.resources_folder_path = os.path.dirname(__file__)

        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.navigation_frame = Frame(self.main_container)
        self.navigation_frame.pack(side=TOP, fill=X)
        self.setup_nav_controls()

        self.navigation_details_frame = Frame(self.main_container)
        self.navigation_details_frame.pack(side=BOTTOM, fill=BOTH)

    def setup_nav_controls(self):
        self.img_icon = Image.open(self.resources_folder_path + "/resources/search.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(resized)
        self.search_button = Button(self.navigation_frame, image=self.search_icon, command=self.search)
        self.search_button.pack(side=RIGHT)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_playlist.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.playlist_icon = ImageTk.PhotoImage(resized)
        self.view_playlists_button = Button(self.navigation_frame, image=self.playlist_icon, command=self.view_playlists)
        self.view_playlists_button.pack(side=RIGHT)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_songs.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.songs_icon = ImageTk.PhotoImage(resized)
        self.view_songs_button = Button(self.navigation_frame, image=self.songs_icon, command=self.view_songs)
        self.view_songs_button.pack(side=RIGHT)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_album.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.albums_icon = ImageTk.PhotoImage(resized)
        self.view_albums_button = Button(self.navigation_frame, image=self.albums_icon, command=self.view_albums)
        self.view_albums_button.pack(side=RIGHT)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_artists.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.artists_icon = ImageTk.PhotoImage(resized)
        self.view_artists_button = Button(self.navigation_frame, image=self.artists_icon, command=self.view_artists)
        self.view_artists_button.pack(side=RIGHT)

    def view_artists(self):
        print("view artists")

    def view_albums(self):
        print("view albums")

    def view_songs(self):
        print("view songs")

    def view_playlists(self):
        print('view playlists')

    def search(self):
        print("search")

    def show_frame(self, screen):
        _list = self.navigation_details_frame.winfo_children()
        for i in _list:
            i.destroy()
        screen(self.navigation_details_frame)