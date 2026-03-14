import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

# response = requests.get("https://www.billboard.com/charts/hot-100/")
# response.raise_for_status()

with open("hot_100.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print(soup.title.string)
tags = soup.select("li ul li h3.c-title")
print([tag.text.strip() for tag in tags])

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=os.environ["SP_CLIENT_ID"],
        client_secret=os.environ["SP_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ["SP_USERNAME"],
    )
)
user_id = sp.current_user()["id"]
print(user_id)
