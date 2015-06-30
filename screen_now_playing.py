__author__ = 'colt'

from tkinter import *
from PIL import Image, ImageTk
import os
import vlc
import settings

class NowPlayingScreen:

    def __init__(self, parent):
        self.resources_folder_path = os.path.dirname(__file__)

        self.main_container = Frame(parent)
        self.main_container.pack(side=TOP, fill=BOTH, expand=True)

        self.control_frame = Frame(self.main_container)
        self.control_frame.pack(side=RIGHT, fill=Y)
        self.setup_controls()

        self.music_details_frame = Frame(self.main_container)
        self.music_details_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.music_titles_frame = Frame(self.music_details_frame)
        self.music_titles_frame.pack(side=TOP)
        self.setup_music_info()

        self.music_timer_frame = Frame(self.music_details_frame)
        self.music_timer_frame.pack(side=BOTTOM, fill=BOTH)
        self.setup_music_timer()

        self.music_art_frame = Frame(self.music_details_frame)
        self.music_art_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.setup_music_art()

        settings.media_player.event_manager().event_attach(vlc.EventType.MediaPlayerMediaChanged, self.update_music_info)
        settings.media_player.event_manager().event_attach(vlc.EventType.MediaPlayerTimeChanged, self.update_time_scale)

        if settings.start_media:
            self.start_media()

        self.update_music_info(event=None)

    def setup_controls(self):
        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_play.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.play_icon = ImageTk.PhotoImage(resized)
        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_pause.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.pause_icon = ImageTk.PhotoImage(resized)
        self.play_pause_button = Button(self.control_frame, command=self.toggle_music)
        if settings.media_list_player.is_playing():
            self.play_pause_button["image"] = self.pause_icon
        else:
            self.play_pause_button["image"] = self.play_icon
        self.play_pause_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_previous.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.prev_icon = ImageTk.PhotoImage(resized)
        self.prev_song_button = Button(self.control_frame, image=self.prev_icon, command=self.prev_song)
        self.prev_song_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_next.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.next_icon = ImageTk.PhotoImage(resized)
        self.next_song_button = Button(self.control_frame, image=self.next_icon, command=self.next_song)
        self.next_song_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_volume_up.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.volume_up_icon = ImageTk.PhotoImage(resized)
        self.volume_increase_button = Button(self.control_frame, image=self.volume_up_icon)
        self.volume_increase_button.pack(side=TOP)

        self.img_icon = Image.open(self.resources_folder_path + "/resources/media_volume_down.png")
        resized = self.img_icon.resize((32, 32), Image.ANTIALIAS)
        self.volume_down_icon = ImageTk.PhotoImage(resized)
        self.volume_decrease_button = Button(self.control_frame, image=self.volume_down_icon)
        self.volume_decrease_button.pack(side=TOP)

        self.total_song_time_label = Label(self.control_frame, text="3:30")
        self.total_song_time_label.pack(side=BOTTOM, fill=X)
        self.current_song_time_label = Label(self.control_frame, text="0:00")
        self.current_song_time_label.pack(side=BOTTOM, fill=X)

    def start_media(self):
        self.play_pause_button["image"] = self.pause_icon
        settings.start_media = False
        settings.media_list_player.play_item(settings.selected_media)

    def toggle_music(self):
        if settings.media_list_player.is_playing():
            self.play_pause_button["image"] = self.play_icon
            settings.media_list_player.pause()
        else:
            self.play_pause_button["image"] = self.pause_icon
            settings.media_list_player.play()

    def prev_song(self):
        if settings.selected_media is not None:
            settings.media_list_player.previous()

    def next_song(self):
        if settings.selected_media is not None:
            settings.media_list_player.next()

    def setup_music_info(self):
        self.song_name_label = Label(self.music_titles_frame, text="No song selected!")
        self.song_name_label.pack(side=TOP, fill=X)
        self.artist_name_label = Label(self.music_titles_frame)
        self.artist_name_label.pack(side=TOP, fill=X)

    def update_music_info(self, event):
        settings.selected_media = settings.media_player.get_media()
        if settings.selected_media is not None:
            title = settings.selected_media.get_meta(vlc.Meta.Title)
            artist = settings.selected_media.get_meta(vlc.Meta.Artist)
            self.song_name_label["text"] = title
            self.artist_name_label["text"] = artist
            self.total_song_time_label["text"] = self.get_media_duration(settings.selected_media.get_duration())
            self.timer_scale["to"] = settings.selected_media.get_duration() // 1000

    def update_time_scale(self, event):
        try:
            ms = settings.media_player.get_time()
            value = ms // 1000
            self.current_song_time_label["text"] = self.get_media_duration(ms)
            self.timer_scale.set(value)
        except Exception:
            return False

    def get_media_duration(self, ms):
        x = ms // 1000
        seconds = x % 60
        x //= 60
        minutes = x % 60
        if seconds < 10:
            seconds = "0" + str(seconds)
        return str(minutes) + ":" + str(seconds)

    def setup_music_art(self):
        photo_file_path = self.resources_folder_path + "/resources/default_album.gif"
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