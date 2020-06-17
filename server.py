from flask import Flask
from youtube.scout.scout import Scout

app = Flask(__name__)

@app.route("/")
def home():
  return { "notice" : "inform the admin about this"}


@app.route("/scout/youtube/today")
def fetchTodayVideos():
  scout = Scout(channel_name="good morning britain", key_word="rashford", all=True)
  # print([{"title" : video.getTitle(), "url" : video.getUrl(), "thumbnail": video.getThumbnail()} for video in scout.findVideos()])
  return {"message": "200 OK", "data" : [{"title" : video.getTitle(), "url" : video.getUrl(), "thumbnail": video.getThumbnail()} for video in scout.findVideos()] }

if __name__ == '__main__':
  app.run(port=3000, host='0.0.0.0')

