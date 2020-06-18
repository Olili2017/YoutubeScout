from pytube import YouTube, Stream

class YouTubeVideo:

  def __init__(self, youtube_link):
    self.__setUrl(youtube_link)
    # self.__video = YouTube(youtube_link)
    # self.__url = self.__video.streams.first().url
    # self.__title = self.__video.title
    # self.__thumbnail = self.__video.thumbnail_url
    # self.__res = [stream for stream in self.__video.streams if stream.resolution == ('360p' if args.get('res', None) == None else args.get('res', None))]

  # def __init__(self, name, url, thumbnail_url):
  #   self.__setTitle(name)
  #   self.__setUrl(url)
  #   self.__setThumbnail(thumbnail_url)

  def getDownloadUrl(self, *urls, **props):
    url = ""
    # check if url given as string argument
    if len(urls) is not 0:
      url = urls[0]
      return self.__scoutDownloadUrl(url)

    # check if key word params are given
    if len(props) is not 0:
      # check if video ID is given
      if props.get("id", None) is not None:
        url = f'https://youtube.com/watch?v={props.get("id", None)}'
        return self.__scoutDownloadUrl(url)

      # check if one time video url is given
      if props.get("url", None) is not None:
        url = props.get("url", None)
        return self.__scoutDownloadUrl(url)

    # use object centric url
    url = self.getUrl()

    self.__scoutDownloadUrl(url)
    # url = f'https://youtube.com/watch?v={args.get("id", None)}' if args.get("id", None) is not None else self.getUrl()
    # print(args)
    # self.__setUrl(args.get("id", self.getUrl()))
    # self.__video = YouTube(youtube_link)
    # self.__url = self.__video.streams.first().url
    # self.__title = self.__video.title
    # self.__thumbnail = self.__video.thumbnail_url
    # self.__res = [stream for stream in self.__video.streams if stream.resolution == ('360p' if args.get('res', None) == None else args.get('res', None))]

  # def getDownloadUrl(self, *args):
  #   print("passing with no namems")
    # return self.getDownloadUrl(url=url)

  def __scoutDownloadUrl(self, url):
    yt = YouTube(url).streams
    return yt.first().url

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


# v = YouTubeVideo('https://www.youtube.com/watch?v=P156VjNAqjY')
# v.getDownloadUrl()