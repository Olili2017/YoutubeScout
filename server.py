from flask import Flask
from youtube.scout.scout import Scout

app = Flask(__name__)

@app.route("/")
def home():
  return { "notice" : "inform the admin about this"}


@app.route("/scout/youtube/today")
def fetchTodayVideos():
  scout = Scout()
  return list(scout.findVideos())

if __name__ == '__main__':
  app.run(port=3000, host='0.0.0.0')