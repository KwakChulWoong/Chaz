import sys
import subprocess
import pytube

yt=pytube.YouTube("https://youtu.be/CTRO5NXmAp8")
video=yt.streams.all()

for i in range(len(video)) :
    print(i, ',',video[i])

down_dir="D:/atom_py"

video[0].download(down_dir)
