from pytube import YouTube, Stream

class YouTubeVideo:

  def __init__(self, youtube_link, **args):
    self.__video = YouTube(youtube_link)
    self.__url = self.__video.streams.first().url
    self.__title = self.__video.title
    self.__thumbnail = self.__video.thumbnail_url
    self.__res = [stream for stream in self.__video.streams if stream.resolution == ('360p' if args.get('res', None) == None else args.get('res', None))]

  def __setUrl(self, url):
    self.__url = url

  def getUrl(self):
    return self.__url

  def __setTitle(self, title):
    self.__title = title

  def getTitle(self):
    return self.__title

  def __setResolution(self, res):
    self.__res[0] = res

  def getResolution(self):
    return self.__res[-1].resolution

  def __setThumbnail(self, thumbnail_url):
    self.__thumbnail = thumbnail_url

  def getThumbnail(self):
    return self.__thumbnail

  def __str__(self):
    return f'Title: {self.getTitle()}\nResolution: {self.getResolution()}'


class ScrapedVideo:

  def __init__(self, name, url, thumbnail_url):
    self.__setTitle(name)
    self.__setUrl(url)
    self.__setThumbnail(thumbnail_url)


  def __setUrl(self, url):
    self.__url = url

  def getUrl(self):
    return self.__url

  def __setTitle(self, title):
    self.__title = title

  def getTitle(self):
    return self.__title

  def __setResolution(self, res):
    self.__res[0] = res

  def getResolution(self):
    return self.__res[-1].resolution

  def __setThumbnail(self, thumbnail_url):
    self.__thumbnail = thumbnail_url

  def getThumbnail(self):
    return self.__thumbnail
