__author__ = 'colt'

from tkinter import *
from PIL import Image, ImageTk
import os
import vlc
import settings
import screen_now_playing

class MusicLibraryScreen:

    def __init__(self, parent):
        self.resources_folder_path = os.path.dirname(__file__)
        self.current_button_selected = None

        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.navigation_frame = Frame(self.main_container)
        self.navigation_frame.pack(side=TOP, fill=X)
        self.setup_nav_controls()

        self.navigation_details_frame = Frame(self.main_container)
        self.navigation_details_frame.pack(side=BOTTOM, fill=BOTH)

        self.view_songs()

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
        self.disable_button(self.view_artists_button)
        self.show_frame(ArtistsBrowseScreen)

    def view_albums(self):
        self.disable_button(self.view_albums_button)
        self.show_frame(AlbumsBrowseScreen)

    def view_songs(self):
        self.disable_button(self.view_songs_button)
        self.show_frame(SongsBrowseScreen)

    def view_playlists(self):
        self.disable_button(self.view_playlists_button)
        self.show_frame(PlaylistsBrowseScreen)

    def search(self):
        print("search")

    def disable_button(self, button):
        if self.current_button_selected is not None:
            self.current_button_selected["state"] = NORMAL
        self.current_button_selected = button
        self.current_button_selected["state"] = DISABLED

    def show_frame(self, screen):
        _list = self.navigation_details_frame.winfo_children()
        for i in _list:
            i.destroy()
        screen(self.navigation_details_frame).pack(side=TOP, fill=BOTH)


class BrowseScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.interior = Frame(self.canvas)
        self.interior.pack(side=TOP, fill=BOTH, expand=True)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)
        self._configure_interior(event=None)
        self._configure_canvas(event=None)

        self.populate()

    def _configure_interior(self, event):
        width = self.interior.winfo_reqwidth()
        height = self.interior.winfo_reqheight()
        self.canvas.config(scrollregion=(0, 0, width, height))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.config(width=self.interior.winfo_reqwidth())
        self.interior.bind('<Configure>', self._configure_interior)

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', self._configure_canvas)

    def populate(self):
        raise NotImplementedError("Please implement this method")

    def item_selected(self, item):
        raise NotImplementedError("Please implement this method")

class ArtistsBrowseScreen(BrowseScreen):

    def __init__(self, parent):
        BrowseScreen.__init__(self, parent)

    def populate(self):
        for x in range(0,33):
            item = "Artist " + str(x)
            button = Button(self.interior, text=item, relief=FLAT, command=lambda i=item: self.item_selected(i))
            button.pack(fill=BOTH)

    def item_selected(self, item):
        print(item + " has been selected")

class SongsBrowseScreen(BrowseScreen):

    def __init__(self, parent):
        BrowseScreen.__init__(self, parent)

    def populate(self):
        total = settings.song_list.count()
        for x in range(0, total):
            settings.song_list.lock()
            item = settings.song_list.item_at_index(x)
            item.parse()
            title = item.get_meta(vlc.Meta.Title)
            settings.song_list.unlock()
            button = Button(self.interior, text=title, relief=FLAT, command=lambda i=item: self.item_selected(i))
            button.pack(fill=BOTH)

    def item_selected(self, item):
        settings.selected_media = item
        settings.main_screen.disable_button(settings.main_screen.nowplaying_button)
        settings.main_screen.show_frame(screen_now_playing.NowPlayingScreen)

class AlbumsBrowseScreen(BrowseScreen):

    def __init__(self, parent):
        BrowseScreen.__init__(self, parent)

    def populate(self):
        for x in range(0,15):
            item = "Album " + str(x)
            button = Button(self.interior, text=item, relief=FLAT, command=lambda i=item: self.item_selected(i))
            button.pack(fill=BOTH)

    def item_selected(self, item):
        print(item + " has been selected")

class PlaylistsBrowseScreen(BrowseScreen):

    def __init__(self, parent):
        BrowseScreen.__init__(self, parent)

    def populate(self):
        for x in range(0,23):
            item = "Playlist " + str(x)
            button = Button(self.interior, text=item, relief=FLAT, command=lambda i=item: self.item_selected(i))
            button.pack(fill=BOTH)

    def item_selected(self, item):
        print(item + " has been selected")