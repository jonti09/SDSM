#!/usr/bin/env python3
import pygame
import os


def get_songs():
    if os.path.exists('/home/pi/project/Data/data/music/songs'):
        os.chdir('/home/pi/project/Data/data/music/songs')
    else:
        exit(0)

    songs = []
    for subdir, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mp3' or '.wav' or '.ogg' or '.wma' or '.aac'):
                songs.append(file)

    return songs[:10]


def play_song(cmd, num):
    pygame.init()
    songs = get_songs()

    if cmd == "play":
        pygame.mixer.music.load(songs[num])
        pygame.mixer.music.play(-1, 0.0)

    if cmd == "next":
        num += 1
        if num == len(songs):
            num = 0

        pygame.quit()
        pygame.init()
        pygame.mixer.music.load(get_songs()[num])
        pygame.mixer.music.play(-1, 0.0)

    elif cmd == "prev":
        num -= 1
        if num == -1:
            num = len(songs)
        pygame.quit()
        pygame.init()
        pygame.mixer.music.load(get_songs()[num])
        pygame.mixer.music.play(-1, 0.0)

    elif cmd == "pause":
        pygame.mixer.music.pause()

    elif cmd == "resume":
        pygame.mixer.music.unpause()

    elif cmd == "last":
        num = len(songs) - 1
        pygame.quit()
        pygame.init()
        pygame.mixer.music.load(get_songs()[num])
        pygame.mixer.music.play(-1, 0.0)

    elif cmd == "stop":
        pygame.quit()
