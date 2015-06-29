__author__ = 'colt'
import vlc

def init():
    global vlc_instance
    vlc_instance = vlc.Instance()

    global song_list
    song_list = vlc_instance.media_list_new()

    global media_list_player
    media_list_player = vlc_instance.media_list_player_new()

    media_list_player.set_media_list(song_list)

    global selected_media
    selected_media = None

    global main_screen
    main_screen = None

