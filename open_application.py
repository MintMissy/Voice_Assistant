# Open application's
import subprocess

# Project modules
import basic_functions

application_list = {
    'spotify': "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk",
    'messenger': "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Messenger.lnk",
    'league of legends': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk",
    'brave': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk",
    'pycharm': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm 2020.3.3.lnk",
    'webstorm': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\WebStorm 2020.3.2.lnk",
    'discord': "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
    'discard': "C:\\Users\Dawid\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
    'microphone': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Iriun Webcam\Iriun Webcam.lnk"
}


def open_app(app):
    subprocess.Popen(application_list[app], shell=True)


def detect_and_open(command):
    # Replace command name to get raw names of apps
    command = command.replace('open ', '')
    command = command.replace('and ', '')

    # Create array with raw names
    if ' ' in command:
        apps_in_command = command.split(' ')
    else:
        apps_in_command = [command]

    apps_to_run = []

    # Find app that are in available dictionary
    for app in apps_in_command:
        if app in application_list:
            apps_to_run.append(app)

    # Stop function if there's no app to run
    if len(apps_to_run) == 0:
        basic_functions.talk("Sorry, I don't see this app on my list")
        return

    # Open apps
    for app in apps_to_run:
        subprocess.Popen(application_list[app], shell=True, startupinfo=None)

    # Tell user which apps are opening
    text_to_tell = "Opening "

    for app in apps_to_run:
        if app == apps_to_run[-1] and len(apps_to_run) > 1:
            text_to_tell += f" and {app}"
        else:
            text_to_tell += f" {app}"

    basic_functions.talk(text_to_tell)
