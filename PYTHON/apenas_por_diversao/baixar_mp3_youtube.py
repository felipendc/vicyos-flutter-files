from pytube import YouTube
from moviepy.editor import *


def baixar_mp3():
    url = input('Insira o link do vídeo: ')
    print('Convertendo...')
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split('.mp4', 1)[0] + f".mp3"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()


baixar_mp3()
