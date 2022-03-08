import pyttsx3 as tts
import speech_recognition

from neuralintents import GenericAssistant
# introduces a recognition software
recognition = speech_recognition.Recognizer()

# introduces the computer speaker
computerSpeaker = tts.init()
computerSpeaker.setProperty("rate", 150)


def recognize_happy():
    print("happy")


def recognize_sad():
    print("sad")
    exec(open("__main__.py").read())


def recognize_angry():
    print("angry")


mappings = {"sad": recognize_sad, "happy": recognize_happy, "angry": recognize_angry()}

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
