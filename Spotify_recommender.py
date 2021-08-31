import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= "ed147dfb315f4ab3a0dbbd0607667f68", client_secret="a1897520673842f99d8261a9d69e604e"))

class Recommender:
    def rec():
        ar = ["rock", "pop", "metalcore", "song", "chill", "dj", "hip-hop", "r&b"]
        results = sp.search(q=random.choice(ar), limit=10)
        for idx, track in enumerate(results['tracks']['items']):
            saying = track["name"], "by",  track["artists"][0]["name"]
            print(saying)

    rec()
