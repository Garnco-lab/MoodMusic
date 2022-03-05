import speech_recognition
import os
from gtts import gTTS
import authorization
import time
import sys
import pandas as pd
import neuralintents
from flask import Flask
from tqdm import tqdm

import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import pywhatkit

from neuralintents import GenericAssistant
import pyttsx3 as tts

spotify = authorization.auth()
genres = spotify.recommendation_genre_seeds()

print(spotify.playback_devices)
# spotify.playback_start_tracks('265Anh9hGoozFigjUVLUeD', offset=None, position_ms=None, device_id='BQAxlnLRpn7GZ6KExeSjVZN3BtAX2dbYsB0BC-IcXsUh35d2gLKgCe7OyhEH9XJ0qbr9RLXnEwHKmnFW2dU')

music_data_dictionary = {
    "id": [],
    "genre": [],
    "track_name": [],
    "artist_name": [],
    "valence": [],
    "energy": [],
    "key": []
}

happy_song_dictionary = {

}

sad_song_dictionary = {

}

for music_genre in tqdm(genres):

    # grabs recommendations
    recommendations = spotify.recommendations(genres=[music_genre], limit=100)
    # imports the json file and then converts it to python readable values
    recommendations = eval(
        recommendations.json()
        .replace("null", "-999")
        .replace("false", "False")
        .replace("true", "True")
    )["tracks"]

    for music_track in recommendations:
        music_data_dictionary["id"].append(music_track["id"])
        music_data_dictionary["genre"].append(music_genre)
        track_meta = spotify.track(music_track["id"])
        music_data_dictionary["track_name"].append(track_meta.name)
        music_data_dictionary["artist_name"].append(track_meta.album.artists[0].name)
        track_features = spotify.track_audio_features(music_track["id"])
        music_data_dictionary["valence"].append(track_features.valence)
        music_data_dictionary["energy"].append(track_features.energy)
        music_data_dictionary["key"].append(track_features.key)

        print(music_data_dictionary["id"])




# introduces a recognition software
recognition = speech_recognition.Recognizer()

# introduces the computer speaker
computerSpeaker = tts.init()
computerSpeaker.setProperty("rate", 150)


def happy():
    print("happy")


def recognize_sad():
    print("sad")


def angry():
    print("angry")


mappings = {"sad": recognize_sad, "happy": happy, "angry": angry}

# The main virtual assistant
virtualAssistant = GenericAssistant("intents.json", intent_methods=mappings)
# trains model automatically from the library
virtualAssistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognition.adjust_for_ambient_noise(mic, duration=0.2)
            voice_audio = recognition.listen(mic)

            messenger = recognition.recognize_google(voice_audio)
            messenger = messenger.lower()

        virtualAssistant.request(messenger)
        # re-instantiate voice
    except speech_recognition.UnknownValueError:
        recognition = speech_recognition.Recognizer()
