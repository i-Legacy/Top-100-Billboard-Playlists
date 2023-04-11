from datetime import datetime
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = env_client_id
CLIENT_SECRET = env_client_secret
SCOPES = "playlist-modify-public"
REDIRECT_URI = "http://localhost:8080/callback"


def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_url(date: str) -> str:
    url = "https://www.billboard.com/charts/hot-100/"
    return url + date


date_input = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
validate_bool = validate_date_format(date_input)

while validate_bool is False:
    date_input = input("\nInvalid date format. Please try again: ")
    validate_bool = validate_date_format(date_input)

try:
    response = requests.get(get_url(date_input))
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error ocurred: {err}")
else:
    billboard_webpage = response.text


container = "o-chart-results-list-row "
title = "c-title"

soup = BeautifulSoup(billboard_webpage, "html.parser")

# Find elements with the specified container class
container_html_elements = soup.select(f".{container}")

# Extract the desired items from the container elements
song_names = []
for elements in container_html_elements:
    # Find elements with title
    items = elements.find_all(class_=title)

    # type(items) -> <class 'bs4.element.ResultSet'> - loops through tags
    # type(item) -> <class 'bs4.element.tag'> has .text attribute
    formatted_items = [item.text.strip().replace("\n", " ") for item in items]
    song_names.extend(formatted_items)


######### SPOTIFY ACCESS
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPES,
    )
)

# Get current user's information
user_info = sp.me()
user_id = user_info["id"]

# Playlist details
playlist_name = f"{date_input} Playlist"
description = "This is a sample playlist created using Spotipy"

# Create a new public playlist
playlist = sp.user_playlist_create(
    user_id, playlist_name, public=True, description=description
)

# Print the playlist details
print("Playlist created successfully:")
print("Name:", playlist["name"])
print("Description:", playlist["description"])
print("Public:", playlist["public"])
print("Owner:", playlist["owner"]["display_name"])

# Search for songs
track_ids = []  # List to store track IDs
for song_name in song_names:
    results = sp.search(q=song_name, type="track", limit=1)  # Search for song
    if results["tracks"]["items"]:
        track_ids.append(
            results["tracks"]["items"][0]["id"]
        )  # Retrieve track ID and add to list

# Add songs to playlist
if track_ids:
    sp.user_playlist_add_tracks(
        user_id, playlist["id"], track_ids
    )  # Add tracks to playlist
    print("Songs added to playlist successfully.")
else:
    print("No songs found to add to playlist.")
