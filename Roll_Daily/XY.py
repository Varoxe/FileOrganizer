import pyautogui
import time

print("Bewegen Sie die Maus an die gewünschte Position.")
time.sleep(5)  # Warten Sie einige Sekunden, um die Position festzulegen
x, y = pyautogui.position()
print(f"Aktuelle Mausposition: x={x}, y={y}")
