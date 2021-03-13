import subprocess
import re

line = "-" * 30

def pass_reveal(method, wifiz):
    if method == "1":
        for wifis in wifiz:
            password = subprocess.run(["netsh", "wlan", "show", "profiles", f'name="{wifis}"', "key=clear"], capture_output = True).stdout.decode()
            pass_capture = (re.findall("Key Content            : (.*)\r", password))
            print(f"{line}\nWiFi: {wifis}\nPassword: {pass_capture}")
        
    elif method == "2":
        name = str(input("Wifi Name: "))
        password = subprocess.run(["netsh", "wlan", "show", "profiles", f'name="{name}"', "key=clear"], capture_output = True).stdout.decode()
        pass_capture = (re.findall("Key Content            : (.*)\r", password))
        print(f"{line}\nWiFi: {name}\nPassword: {pass_capture}")
        
        

def start():
    wifis = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    wifi_names = (re.findall("All User Profile     : (.*)\r", wifis))
    print(f"Hello and Welcome to WiFi Pass Revealer! Let's take a look at your WiFi's!\n{line}")
    for wifis in wifi_names:
        print(f"Available WiFi: {wifis}")
        
    method = input(f"{line}\nChoose a method please\n\n 1 - Reveal All\n 2 - Reveal by Name\n\nMethod: ")
    pass_reveal(method, wifi_names)
    
start()
