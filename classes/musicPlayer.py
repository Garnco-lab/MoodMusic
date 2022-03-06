import re
import requests
import urllib.parse
import urllib.request

import pafy

import vlc
from bs4 import BeautifulSoup


class MusicPlayer:
    def __init__(self):
        self.artist_name = ""
        self.track_name = ""

    def play_music(self, artist, track):
        self.artist_name = artist
        self.track_name = track
        music = self.artist_name + " " + self.track_name
        query = urllib.parse.urlencode({"search_query": music})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query)

        results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get(
            "https://www.youtube.com/watch?v=" + "{}".format(results[0])
        )
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(results[0])

        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")

        for concatMusic1 in yt_title:
            pass
        url = clip2
        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
