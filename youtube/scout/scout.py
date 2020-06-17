from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from youtube.scout.type import ScoutType
import time

class Scout:

  site = 'https://youtube.com'
  videos = set()

  def __init__(self, **args):
    self.type = args.get('type', ScoutType.TODAY)
    self.channel_name = args.get('channel_name', "Next Media Uganda")
    self.key_word = args.get('key_word', "uncut")
    self.get_all_videos = args.get('all', False)

  def loadDriver(self):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    self.chrome = webdriver.Chrome(chrome_options=options)

  def __getDriver(self):
    return self.chrome

  def findVideos(self):
    self.loadDriver()

    # make call to youtube
    self.__getDriver().get(self.site)

    # open youtube and search item
    self.__searchOnYouTube(self.channel_name + ' ' + self.key_word)

    # open filter
    self.__getDriver().find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()

    if self.type is ScoutType.LAST_HOUR:
      return self.__findVideosInPastPastHour()

    if self.type is ScoutType.TODAY:
      return self.__findVideosInPastPastDay()

    if self.type is ScoutType.THIS_WEEK:
      return self.__findVideosInPastPastWeek()

    if self.type is ScoutType.THIS_MONTH:
      return self.__findVideosInPastPastMonth()

    if self.type is ScoutType.THIS_YEAR:
      return self.__findVideosInPastPastYear()

    self.chrome.close()
    return None

  def __findVideosInPastPastDay(self):
    # click on filter Today option
    self.__getDriver().find_element_by_xpath('//*[@title="Search for Today"]').find_element_by_xpath('..').click()

    return self.__scrapeVideos()

  def __findVideosInPastPastHour(self):
    # click on filter Past hour option
    self.__getDriver().find_element_by_xpath('//*[@title="Search for Last hour"]').find_element_by_xpath('..').click()

    return self.__scrapeVideos()

  def __findVideosInPastPastWeek(self):
    # click on filter Past week option
    self.__getDriver().find_element_by_xpath('//*[@title="Search for This week"]').find_element_by_xpath('..').click()

    return self.__scrapeVideos()

  def __findVideosInPastPastMonth(self):
    # click on filter Past month option
    self.__getDriver().find_element_by_xpath('//*[@title="Search for This month"]').find_element_by_xpath('..').click()

    return self.__scrapeVideos()

  def __findVideosInPastPastYear(self):
    # click on filter Past year option
    self.__getDriver().find_element_by_xpath('//*[@title="Search for This year"]').find_element_by_xpath('..').click()

    return self.__scrapeVideos()

  def __searchOnYouTube(self, search_text: str):
    search_box = self.__getDriver().find_element_by_xpath('//input[@id="search"]')
    search_box.send_keys(search_text)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

  def __scrapeVideos(self):
    time.sleep(1)
    result_container = self.__getDriver().find_element_by_xpath('//*[@class="style-scope ytd-item-section-renderer"]/div')
    results = result_container.find_elements_by_xpath('//div[@id="contents"]/ytd-video-renderer')
    # print(str(results.innerHTML))
    for result in results:
      title = result.find_element_by_xpath('.//a[@id="video-title"]')
      if self.get_all_videos:
        self.videos.add(title.get_attribute('href'))
        continue
      if self.key_word in title.get_attribute('title').lower():
        self.videos.add(title.get_attribute('href'))
    return self.videos
