import speech_recognition

import authorization
import time
import sys
import pandas as pd
import neuralintents
from neuralintents import GenericAssistant
import pyttsx3 as tts

recognition = speech_recognition.Recognizer()

computerSpeaker = tts.init()
computerSpeaker.setProperty('rate', 150)
