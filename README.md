🎯 Remote Device Control System (Python Socket Backdoor)
⚠️ For Educational and Authorized Use Only
This project is intended solely for educational, research, and authorized penetration testing purposes. Do not use it on devices you do not own or without explicit permission.

🛠 Overview
This is a lightweight remote control system built using Python sockets. It consists of a server (back.py) and a client (client.py) that allows the operator to remotely interact with a device over a local network or exposed IP.

📦 Features
✅ Controller (back.py)
Listens for incoming connections

Displays a full ASCII banner on client connect

Provides a control menu with the following options:

1.Exit

2.Restart remote device

3.Take a webcam photo

4.Get geolocation (via IP)

5.Take a screenshot

6.List files in the current directory

7.Show a custom popup message
-
------------------------------------------------------------------------


✅ Client (client.py)
*Connects to the controller via IP and port

*Executes commands received from the server:

*Reboots the machine using system commands

*Uses OpenCV to capture webcam images

*Takes screenshots with pyautogui

*Fetches location data using ipinfo.io

*Shows popup messages using PowerShell (Windows only)

*Sends back a list of current directory contents
-
------------------------------------------------------------------------


⚙️ Tech Stack
*socket – For TCP communication

*OpenCV – For webcam integration

*pyautogui – For taking screenshots

*requests – For retrieving public IP location

*os, PowerShell – For system-level operations
-
------------------------------------------------------------------------
🧠 Use Cases
*Educational demonstrations in cybersecurity labs

*Red team simulation and training

*Parental control / authorized remote support

*Prototyping lightweight remote monitoring tools
-
------------------------------------------------------------------------
Install dependencies:
<pre> pip install -r requirements.txt  </pre>

<pre> pip install opencv-python -i https://mirrors.aliyun.com/pypi/simple/  </pre>

<pre> pip3 install pillow -i https://pypi.tuna.tsinghua.edu.en/simple/  </pre>
<pre>pip3 install pyinstaller -i https://pypi.tuna.tsinghua.edu.en/simple/  </pre>
-
------------------------------------------------------------------------

🛑 This project is not stealthy and is easily detectable. It is for learning purposes only.

🛡 Legal & Ethical Notice
🚨 Do NOT use this tool on devices you don’t own or without explicit written permission.

🚨 Unauthorized access to systems is illegal and unethical.

🚨 The author assumes no liability for misuse.
