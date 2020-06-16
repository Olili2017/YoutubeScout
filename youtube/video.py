from pytube import YouTube, Stream

class YouTubeVideo:
  
  def __init__(self, youtube_link, **args):
    self.video = YouTube(youtube_link)
    self.url = self.video.streams.first().url
    self.title = self.video.title
    self.thumbnail = self.video.thumbnail_url
    self.res = [stream for stream in self.video.streams if stream.resolution == ('360p' if args.get('res', None) == None else args.get('res', None))]

  def getUrl(self):
    return self.url

  def getTitle(self):
    return self.title

  def getResolution(self):
    return self.res[-1].resolution

  def __str__(self):
    return f'Title: {self.getTitle()}\nResolution: {self.getResolution()}'