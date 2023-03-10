
try:
    import time
    import colorama
    import requests
    import time
    import requests
    import json
    import re
    import configparser
    from cleantext import clean
    import os
    from colorama import init, Fore, Back, Style
    init()
# If user doesn't have one of the modules, it will tell them to install all of the required
except ImportError:
    print("[ERROR] Failed to import some modules, make sure to run requirements.bat, delete all other python versions and install python 3.10.0 installed with add to path option checked during installation")
    input()

print(f"{Back.BLACK}{Fore.RED}                 ___.    .__                      __                                                               ")
time.sleep(0.1)
print(f"{Back.BLACK}{Fore.RED}__  _  __  ____  \_ |__  |  |__    ____    ____  |  | __   ____________  _____     _____    _____    ____  _______ ")
time.sleep(0.1)
print(f"{Back.BLACK}{Fore.RED}\ \/ \/ /_/ __ \  | __ \ |  |  \  /  _ \  /  _ \ |  |/ /  /  ___/\____ \ \__  \   /     \  /     \ _/ __ \ \_  __  ")  
time.sleep(0.1)
print(f"{Back.BLACK}{Fore.RED} \     / \  ___/  | \_\ \|   Y  \(  <_> )(  <_> )|    <   \___ \ |  |_> > / __ \_|  Y Y  \|  Y Y  \\  ___/  |  | \/")
time.sleep(0.1)
print(f"{Back.BLACK}{Fore.RED}  \/\_/   \___  > |___  /|___|  / \____/  \____/ |__|_ \ /____  >|   __/ (____  /|__|_|  /|__|_|  / \___  > |__|   ")
time.sleep(0.1)
print(f"{Back.BLACK}{Fore.RED}              \/      \/      \/                      \/      \/ |__|         \/       \/       \/      \/         ")
time.sleep(0.1)
print("made by jordan")
print(" ")

hook = input("enter discord webhook here: ")

print(" ")

webhook_url = hook  # Replace with your own webhook URL

msg = input("what do you want to say: ")

while True:
    message = {
        "content": msg  # Replace with your own message content
    }

    json_payload = json.dumps(message)

    response = requests.post(webhook_url, data=json_payload, headers={"Content-Type": "application/json"})

    if response.status_code == 204:
        print("Message sent successfully.")
        print(" ")
    else:
        print(f"Error sending message: {response.text}")

    # Wait for some time before sending the next message
