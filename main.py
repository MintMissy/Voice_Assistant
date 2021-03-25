# Microphone detecting
import speech_recognition
# Open application's
import subprocess
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
# Working with websites
from selenium import webdriver


def get_current_time():
    """
    Get current time
    :return: current time (hour; minute; AM/PM)
    """
    return datetime.datetime.today().strftime("%H:%M %p")


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
            talk(f"it is {get_current_time()}")

        elif 'song' in command:
            # Play music on youtube
            if 'play' in command:
                driver_path = "C:\\01 Programming\Python\Mintsy Assistant\chromedriver.exe"
                brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"

                option = webdriver.ChromeOptions()
                option.binary_location = brave_path
                brave_options = "user-data-dir=C:\\Users\Dawid\AppData\Local\BraveSoftware\Brave-Browser\\Music"
                option.add_argument(brave_options)

                browser = webdriver.Chrome(executable_path=driver_path, options=option)

                driver = browser.get("https://www.youtube.com/watch?v=jJPMnTXl63E")

        elif 'open' in command:
            if 'spotify' in command:
                talk('opening spotify')
                subprocess.Popen("C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk",
                                 shell=True)

            elif 'messenger' in command:
                talk('opening messenger')
                subprocess.Popen("C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Messenger.lnk",
                                 shell=True)

            elif 'league of legends' in command:
                talk('opening league of legends')
                subprocess.Popen(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk",
                    shell=True)

            elif 'brave' in command:
                talk('opening brave')
                subprocess.Popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk",
                                 shell=True)

            elif 'pycharm' in command:
                talk('opening pycharm')
                subprocess.Popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm 2020.3.3.lnk",
                                 shell=True)

            elif 'webstorm' in command:
                talk('opening webstorm')
                subprocess.Popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\WebStorm 2020.3.2.lnk",
                                 shell=True)

            elif 'discord' in command:
                talk('opening discord')
                subprocess.Popen(
                    "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
                    shell=True)


talk('Hello Mint Missy')
subprocess.Popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Iriun Webcam\Iriun Webcam.lnk", shell=True)

listener = get_microphone()

time.sleep(8)
talk('I am ready to go')

while True:
    if round(time.time()) % 120 == 0:
        listener = get_microphone()
    run_assistant()
