import speech_recognition
import os
from gtts import gTTS
import authorization
import time
import sys
import pandas as pd
import neuralintents

from neuralintents import GenericAssistant
import pyttsx3 as tts

# introduces a recognition software
recognition = speech_recognition.Recognizer()

# introduces the computer speaker
computerSpeaker = tts.init()
computerSpeaker.setProperty('rate', 150)


def happy():
    print("happy")

def recognize_sad():
    print("sad")

def angry():
    print("angry")


mappings = {
    'sad': recognize_sad,
    'happy': happy,
    'angry': angry
}

# The main virtual assistant
virtualAssistant = GenericAssistant('intents.json', intent_methods=mappings)
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
