import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= "CLIENT_ID", client_secret="CLIENT_SECRET"))

class Recommender:
    def rec():
        ar = ["rock", "pop", "metalcore", "song", "chill", "dj", "hip-hop", "r&b"]
        results = sp.search(q=random.choice(ar), limit=10)
        for idx, track in enumerate(results['tracks']['items']):
            saying = track["name"], "by",  track["artists"][0]["name"]
            print(saying)

    rec()
