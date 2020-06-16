import video

vid = video.YouTubeVideo('https://www.youtube.com/watch?v=P156VjNAqjY', res='360p')

# print(vid.getUrl())
# print(vid.getResolution())

print(vid.__str__())
