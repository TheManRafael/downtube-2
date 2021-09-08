from pytube import YouTube
import os


def downTubeVideo(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    print(yt.title)


def downTubeMusic(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(only_audio=True).first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


video = input("Digite o link do vídeo desejado: ")
confirm = input("Deseja baixar só o audio? s/n: ")
user = input("Digite o nome do seu usuário: ")


if confirm == "s":
    path = (f"/home/{user}/Música/DownTube")
    downTubeMusic(video, path)
    print(f"Salvo em {path}")
elif confirm == "n":
    path = (f"/home/{user}/Vídeos/DownTube")
    downTubeVideo(video, path)
    print(f"Salvo em {path}")
