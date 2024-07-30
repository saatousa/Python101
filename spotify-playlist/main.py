from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentications
CLIENT_ID = "..."
CLIENT_SECRET = "..."
REDIRECT_URI = "https://example.com"
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               cache_path="token.txt",
                                               show_dialog=True))

user_id = sp.current_user()

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = int(user_date.split("-")[0])

response = requests.get(f"{BILLBOARD_URL}/{user_date}")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_titles = soup.select("li ul li h3")

songs_list = [song.getText().strip() for song in song_titles]
uri_list = []

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(uri_list)

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
