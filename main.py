import random
import pyttsx3 as tts
import speech_recognition

from neuralintents import GenericAssistant
from tqdm import tqdm

from classes import musicPlayer

import authorization

mood_value = 0.15

playmusic = musicPlayer.MusicPlayer()


spotify = authorization.auth()
genres = spotify.recommendation_genre_seeds()

track_count = 0

music_data_dictionary = {
    "id": [],
    "track_name": [],
    "artist_name": [],
    "valence": [],
    "energy": [],
    "danceability": [],
}


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

print(music_data_dictionary[0])

selection = random.randint(0, len(music_data_dictionary["artist_name"]) - 1)

playmusic.play_music(
    music_data_dictionary["artist_name"][selection],
    music_data_dictionary["track_name"][selection],
)

