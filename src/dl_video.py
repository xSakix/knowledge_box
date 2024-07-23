from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=VazI1uNGPmI")

print(yt.title)
print(yt.streams)

stream = yt.streams.get_by_itag(140)
stream.download(filename="diskusia.mp4")