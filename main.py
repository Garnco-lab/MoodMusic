import random
from tqdm import tqdm
from classes import musicPlayer
import authorization
import pandas as pd
import csv

# the initial mood value on how you want to feel, this will be updatable in the final application
mood_value = 0.15

# the music player
playmusic = musicPlayer.MusicPlayer()

# grabbing spotify authorization and then picking genres from a variety
spotify = authorization.auth()
genres = spotify.recommendation_genre_seeds()

# the track counter, currently unused
track_count = 0

# music data to be converted to a csv using a dictionary object
music_data_dictionary = {
    "id": [],
    "track_name": [],
    "artist_name": [],
    "valence": [],
    "energy": [],
    "danceability": [],
}

# iterate and grab random songs, pushing them into the dictionary object with individual lists
for music_genre in tqdm(genres):

    # grabs recommendations
    recommendations = spotify.recommendations(genres=[music_genre], limit=1)
    # imports the json file and then converts it to python readable values
    recommendations = eval(
        recommendations.json()
        .replace("null", "-999")
        .replace("false", "False")
        .replace("true", "True")
    )["tracks"]

    for music_track in recommendations:
        music_data_dictionary["id"].append(music_track["id"])
        track_meta = spotify.track(music_track["id"])
        music_data_dictionary["track_name"].append(track_meta.name)
        music_data_dictionary["artist_name"].append(track_meta.album.artists[0].name)
        track_features = spotify.track_audio_features(music_track["id"])
        music_data_dictionary["valence"].append(track_features.valence)
        music_data_dictionary["energy"].append(track_features.energy)
        music_data_dictionary["danceability"].append(track_features.danceability)

# convert music data dictionary object to a csv using pandas
dataframe = pd.DataFrame(music_data_dictionary)
dataframe.drop_duplicates(subset="id", keep="first", inplace=True)
dataframe.to_csv("music_dataset.csv", index=False)

csv_to_iterate_over = "music_dataset.csv"

# add mood iterations here
with open(csv_to_iterate_over, 'r', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)
    for row in datareader:
        print(row[2] + " " + row[1])

# select a random song, this will be updated to select one out of a specific mood
selection = random.randint(0, len(music_data_dictionary["artist_name"]) - 1)

# play the selected song from in audio using vlc and youtube-dl to get audio, effectively giving you the full song
playmusic.play_music(
    music_data_dictionary["artist_name"][selection],
    music_data_dictionary["track_name"][selection],
)
