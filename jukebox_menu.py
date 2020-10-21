from typing import ClassVar
from nested_data import albums

SONGS_LIST_INDEX = 3  # CONSTANT DATA is in all caps
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title,))
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index + 1, title, artist, year, songs)   YAPMANIN BAŞKA UZUN YOLU
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song (invalid choice goes back to the album list):")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("="*40)
