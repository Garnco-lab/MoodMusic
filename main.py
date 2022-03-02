import speech_recognition

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

# The main virtual assistant
virtualAssistant = GenericAssistant('intents.json')
# trains model automatically from the library
virtualAssistant.train_model()
