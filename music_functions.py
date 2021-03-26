# Working with websites
from selenium import webdriver

driver_path = "C:\\01 Programming\Python\Mintsy Assistant\chromedriver.exe"
brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
brave_data = "user-data-dir=C:\\Users\Dawid\AppData\Local\BraveSoftware\Brave-Browser\\Music"

# Create custom options for brave
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument(brave_data)


def play_music():
    # Apply custom options and open browser
    browser = webdriver.Chrome(executable_path=driver_path, options=option)

    # Open music in browser
    driver = browser.get("https://www.youtube.com/watch?v=jJPMnTXl63E")
