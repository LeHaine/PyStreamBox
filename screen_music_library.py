__author__ = 'colt'

from tkinter import *

class MusicLibraryScreen:

    def __init__(self, parent):
        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.navigation_frame = Frame(self.main_container)
        self.navigation_frame.pack(side=TOP, fill=X)
        self.setup_nav_controls()

        self.navigation_details_frame = Frame(self.main_container)
        self.navigation_details_frame.pack(side=BOTTOM, fill=BOTH)


    def setup_nav_controls(self):
        self.view_artists_button = Button(self.navigation_frame, text="Artists", command=self.view_artists)
        self.view_artists_button.pack(side=LEFT)
        self.view_albums_button = Button(self.navigation_frame, text="Albums", command=self.view_albums)
        self.view_albums_button.pack(side=LEFT)
        self.view_songs_button = Button(self.navigation_frame, text="Songs", command=self.view_songs)
        self.view_songs_button.pack(side=LEFT)
        self.view_playlists_button = Button(self.navigation_frame, text="Playlists", command=self.view_playlists)
        self.view_playlists_button.pack(side=LEFT)
        self.search_button = Button(self.navigation_frame, text="Search", command=self.search)
        self.search_button.pack(side=LEFT)

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