import subprocess
import pyautogui
import time
import win32api, win32con
import keyboard

# Pfad zur Chrome-Exe-Datei
chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# URL zur Webseite
url = "https://www.csgoroll.com/en/boxes/world/daily-free"

# Funktion zum Öffnen der Webseite in Chrome
def open_webpage():
    subprocess.call([chrome_path, url])
    time.sleep(3)
    pyautogui.scroll(-scroll_steps)  # Scrollen auf der Webseite
    time.sleep(5)

# Funktion zum Klicken
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # Pause, um den Klick zu simulieren
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Funktion, um Koordinaten basierend auf dem Level zurückzugeben
def get_coordinates(level):
    coordinates = {
        10: (783, 215),
        20: (1080, 211),
        30: (1355, 212),
        40: (1733, 215),
        50: (476, 599),
        60: (770, 600),
        70: (1107, 598),
        80: (1407, 596)
    }
    return coordinates.get(level, (None, None))

# Funktion zum Klicken auf eine bestimmte Position
def click_at_level(level):
    x, y = get_coordinates(level)
    if x is not None and y is not None:
        click(x, y)

scroll_steps = 980

# Schleife zur Ausführung der Klicks
while not keyboard.is_pressed('q'):
    open_webpage()  # Öffnen der Webseite
    for level in [10, 20, 30, 40, 50, 60, 70, 80]:
        click_at_level(level)
        time.sleep(1)  # Pause zwischen den Klicks
        open_webpage()  # Zurück zur Hauptseite und erneut öffnen
