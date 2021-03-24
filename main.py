import speech_recognition
import pyttsx3
import subprocess
import sys

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speech_recognition.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'assistant' in command:
                command = command.replace('assistant', '')
                return command
    except Exception:
        pass


def run_assistant():
    command = take_command()
    if command is not None:
        if 'open' in command:
            if 'spotify' in command:
                talk('opening spotify')
                program = subprocess.Popen(
                    "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk", shell=True)

            elif 'messenger' in command:
                talk('opening messenger')
                program = subprocess.Popen(
                    "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Messenger.lnk", shell=True)

            elif 'league of legends' in command:
                talk('opening league of legends')
                program = subprocess.Popen(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk", shell=True)

            elif 'brave' in command:
                talk('opening brave')
                program = subprocess.Popen(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk", shell=True)

            elif 'pycharm' in command:
                talk('opening pycharm')
                program = subprocess.Popen(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm 2020.3.3.lnk", shell=True)

            elif 'webstorm' in command:
                talk('opening webstorm')
                program = subprocess.Popen(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\WebStorm 2020.3.2.lnk", shell=True)

            elif 'discord' in command:
                talk('opening discord')
                program = subprocess.Popen(
                    "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
                    shell=True)


while True:
    run_assistant()
