__author__ = 'colt'

from tkinter import *


class PlaylistSettings:

    def __init__(self, parent):
        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.playlist_setting_controls_frame = Frame(self.main_container)
        self.playlist_setting_controls_frame.pack(side=TOP, fill=BOTH)

        self.display_playlist_setting_controls()

    def display_playlist_setting_controls(self):
        self.create_playlist_button = Button(self.playlist_setting_controls_frame, text="Create New Playlist",
                                             command=self.create_playlist)
        self.create_playlist_button.pack(side=TOP, fill=X, pady=20, padx=15)

        self.delete_playlist_button = Button(self.playlist_setting_controls_frame, text="Delete Playlist",
                                             command=self.delete_playlist)
        self.delete_playlist_button.pack(side=TOP, fill=X, pady=20, padx=15)

        self.edit_playlist_button = Button(self.playlist_setting_controls_frame, text="Edit Playlist",
                                           command=self.edit_playlist)
        self.edit_playlist_button.pack(side=TOP, fill=X, pady=20, padx=15)

    def create_playlist(self):
        print("create playlist")

    def delete_playlist(self):
        print("delete playlist")

    def edit_playlist(self):
        print("edit playlist")



class CreatePlaylistScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

class DeletePlaylistScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

class EditPlaylistScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)