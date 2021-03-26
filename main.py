# Time modules
import datetime
import time
# Microphone detecting
import speech_recognition

# Project modules
import open_application
import time_functions
import music_functions
import basic_functions


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

            assistant_names = ['vicky', 'vicki', 'viki', 'vk', 'ricky']

            # If user said assistant name return command
            for name in assistant_names:
                if name in command:
                    command = command.replace(name, '')
                    return command
    except Exception:
        pass


def run_assistant():
    command = take_command()

    if command is not None:
        # Get current time EXAMPLE QUESTION 'what time is it'
        if 'time' in command and 'what' in command:
            basic_functions.talk(f"it is {time_functions.get_current_time()}")

        elif 'song' in command:
            if 'play' in command:
                music_functions.play_music()

        elif 'music' in command:
            pass

        elif 'open' in command:
            # Open application by command
            open_application.detect_and_open(command)

        # Funny things :3
        elif 'kill you' in command:
            basic_functions.talk('You\'re not allowed to do that')

        elif 'say' in command:
            command = command.replace("say ", "")
            basic_functions.talk(command)


# Start of the program
basic_functions.talk('Hello Mint Missy')
# Open my phone microphone
open_application.open_app('microphone')

# Get microphone object
listener = speech_recognition.Recognizer()

# Wait before my phone connect with PC and inform user that he can start saying commands
time.sleep(7)
basic_functions.talk('I am ready to go')

while True:

    # Refreshing microphone object (sometimes it crashes)
    # if round(time.time()) % 5 == 0:
    #     listener = speech_recognition.Recognizer()
    #     print("microphone refreshed")

    # Listening for commands
    run_assistant()
