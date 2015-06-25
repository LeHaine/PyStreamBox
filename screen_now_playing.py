__author__ = 'colt'

from tkinter import *
from PIL import Image, ImageTk
import os

class NowPlayingScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.music_on = False
        self.main_container = Frame(parent, background="blue")
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.control_frame = Frame(self.main_container, background="red")
        self.control_frame.pack(side=RIGHT, fill=Y)
        self.setup_controls()

        self.music_details_frame = Frame(self.main_container, background="purple")
        self.music_details_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.music_titles_frame = Frame(self.music_details_frame, background="black")
        self.music_titles_frame.pack(side=TOP)
        self.setup_music_info()

        self.music_timer_frame = Frame(self.music_details_frame, background="orange")
        self.music_timer_frame.pack(side=BOTTOM, fill=BOTH)
        self.setup_music_timer()

        self.music_art_frame = Frame(self.music_details_frame, background="blue")
        self.music_art_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.setup_music_art()



    def setup_controls(self):
        self.play_pause_button = Button(self.control_frame, text="Play", command=self.toggle_music)
        self.play_pause_button.pack(side=TOP)
        self.prev_song_button = Button(self.control_frame, text="Prev")
        self.prev_song_button.pack(side=TOP)
        self.next_song_button = Button(self.control_frame, text="Next")
        self.next_song_button.pack(side=TOP)
        self.volume_increase_button = Button(self.control_frame, text="+")
        self.volume_increase_button.pack(side=TOP)
        self.volume_decrease_button = Button(self.control_frame, text="-")
        self.volume_decrease_button.pack(side=TOP)
        self.total_song_time_label = Label(self.control_frame, text="3:30")
        self.total_song_time_label.pack(side=BOTTOM, fill=X)
        self.current_song_time_label = Label(self.control_frame, text="0:00")
        self.current_song_time_label.pack(side=BOTTOM, fill=X)

    def toggle_music(self):
        if self.music_on:
            self.music_on = False
            self.play_pause_button["text"] = "Play"
        else:
            self.music_on = True
            self.play_pause_button["text"] = "Pause"

    def setup_music_info(self):
        self.song_name_label = Label(self.music_titles_frame, text="Song Name")
        self.song_name_label.pack(side=TOP, fill=X)
        self.artist_name_label = Label(self.music_titles_frame, text="Artist Name")
        self.artist_name_label.pack(side=TOP, fill=X)

    def setup_music_art(self):
        photo_file_path = os.path.dirname(__file__) + "/resources/default_album.gif"
        self.image = Image.open(photo_file_path)
        self.img_copy = self.image.copy()

        self.album_photo = ImageTk.PhotoImage(self.image)
        self.album_photo_label = Label(self.music_art_frame, image=self.album_photo)
        self.album_photo_label.image = self.album_photo
        self.album_photo_label.pack(side=TOP, fill=BOTH)
        self.album_photo_label.bind("<Configure>", self._resize_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height
        """Keeps the image a square"""
        if new_width > new_height:
            new_width = new_height
        elif new_height > new_width:
            new_height = new_width

        self.image = self.img_copy.resize((new_width, new_height))
        self.album_photo = ImageTk.PhotoImage(self.image)
        self.album_photo_label.configure(image=self.album_photo)

    def setup_music_timer(self):
        self.timer_scale = Scale(self.music_timer_frame, from_=0, to=100, orient=HORIZONTAL)
        self.timer_scale.pack(side=TOP, fill=BOTH)
