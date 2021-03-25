# Microphone detecting
import speech_recognition
# Time modules
import datetime
import time
# Play sound to user
import playsound
# Working on directory's
import os
import random
# Google text to speech
from gtts import gTTS


# Project modules
import open_application
import time_functions
import music_functions


def get_microphone():
    """
    Get microphone from user
    :return: microphone
    """
    return speech_recognition.Recognizer()


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


def take_command():
    """
    Take user voice, if there's assistant name returns command
    :return: command
    """
    try:
        with speech_recognition.Microphone() as source:
            # Convert voice into text
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            # Log command
            print("[LOG]" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M %p')) + " " + command)

            # If user said assistant name return command
            if 'vicky' in command or 'vicki' in command:
                command = command.replace('vicky', '')
                command = command.replace('vicki', '')
                return command
    except Exception:
        pass


def run_assistant():
    command = take_command()

    if command is not None:
        # Get current time EXAMPLE QUESTION 'what time is it'
        if 'time' in command and 'what' in command:
            talk(f"it is {time_functions.get_current_time()}")

        elif 'song' in command:
            if 'play' in command:
                music_functions.play_music()

        elif 'music' in command:
            pass

        elif 'open' in command:
            # Open application by command
            open_application.detect_and_open(command)


# Start of the program
talk('Hello Mint Missy')
# Open my phone microphone
open_application.open_app('microphone')

# Get microphone object
listener = get_microphone()

# Wait before my phone connect with PC and inform user that he can start saying commands
time.sleep(8)
talk('I am ready to go')

while True:
    # Refreshing microphone object (sometimes it crashes)
    if round(time.time()) % 120 == 0:
        listener = get_microphone()

    # Listening for commands
    run_assistant()
