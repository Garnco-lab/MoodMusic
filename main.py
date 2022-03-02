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


def helloWorld():
    print("hello world")

def recognize_sad():
    computerSpeaker.say("Okay lets play something sad")
    myobj = gTTS(text="my text", lang='en', slow=False)
    myobj.save("super.mp3")
    os.system("super.mp3")
    print("this worked")


mappings = {
    'sad': recognize_sad,
    'happy': helloWorld,
    'angry': helloWorld
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
