import os
line = "-" * 30

def password(wifi_name):
    os.system(f'netsh wlan show profiles name="{wifi_name}" key="clear"')
    os.system("cls")
    
def start():
    os.system("cls")
    print(f"{line}\nWelcome to WiFi Password finder.\nPlease select the WiFi that you want to show password of.\n{line}\nAvailable WiFi's are listed above.\n{line}")
    os.system("netsh wlan show profiles", capture)
    wifi = str(input(f"{line}\nWiFi Name: "))
    password(wifi)
    
start()
