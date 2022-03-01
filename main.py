import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Trying to figure out authorization scope using online examples

client_id='your_spotify_client_id'
client_secret='your_spotify_client_secret'
redirect_uri='your_url_to_redirect'
username = 'your_username_spotify_code'
scope = 'playlist-modify-public'