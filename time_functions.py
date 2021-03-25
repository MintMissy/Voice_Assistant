# Time modules
import datetime
import time


def get_current_time():
    """
    Get current time
    :return: current time (hour; minute; AM/PM)
    """
    return datetime.datetime.today().strftime("%H:%M %p")
