import sounddevice as sd
import scipy.io.wavfile as wav
import pygame
import os
import time

FILEPATH = "assets\music\music.mp3"
fs = 44100
seconds = 3


def record_sound(seconds, filepath):
    data = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    wav.write(filepath, fs, data)
    print(f"Запись сохранена в {filepath}")
    return filepath


def play_sound(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Важно: выгружаем файл из памяти, чтобы Windows разрешила его удалить
    pygame.mixer.music.unload()
    pygame.mixer.quit()

    # Удаляем файл
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Файл {filepath} успешно удален.")


def play_music(filepath=FILEPATH, wait=False):
    pygame.mixer.init()
    music = pygame.mixer.Sound(filepath)
    channel = pygame.mixer.Channel(1)
    channel.play(music, -1)
    if wait:
        while channel.get_busy():
            time.sleep(0.1)

    return channel


play_music(wait=True)
