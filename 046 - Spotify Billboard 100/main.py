from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = "XXXXXXXXXXXXXX"
SPOTIFY_CLIENT_SECRET = "XXXXXXXXXXXXXX"
REDIRECT_URI = "http://127.0.0.1:5500/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="authToken.txt",
    )
)
user_id = sp.current_user()["id"]

date_pick = input(f"Which year do you want to travel to?\n"
                  f"Type the date in this format YYYY-MM-DD:\n")

response = requests.get(f"{BILLBOARD_URL}/{date_pick}")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

search_all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_titles = [song.getText() for song in search_all_songs]

year = date_pick.split("-")[0]

song_uris = []

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date_pick} Billboard 100",
    public=False
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
