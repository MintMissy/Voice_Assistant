import random
# Working on directory's
import os
# Play sound to user
import playsound
# Google text to speech
from gtts import gTTS


def get_microphone():
    """
    Get microphone from user
    :return: microphone
    """
    pass
    # return speech_recognition.Recognizer()


def talk(text):
    """
    Talk to user (sound)
    :param text: text to talk
    """
    tts = gTTS(text=text, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
