import webbrowser
import requests
from colorama import Fore, Back, Style
import urllib.request
headerss = {
    'User-Agent': 'yehorscode/Umimc (umimc@proton.me)'
}
import json
import http

print(Fore.MAGENTA + "Welcome to Unimc! Universal Minecraft Mod installer!", Fore.RESET)
print(Back.CYAN + "Select your mode:" + Back.RESET)
print(Back.CYAN +
    """
1: Installing, here you can install mods from Modrinth!
2: Remove .minecraft/mods folder (removes all mods)"""+Back.RESET)

labrinthapi = requests.get("https://api.modrinth.com/v2/search?query=create",headers=headerss)
labrinthapi.raise_for_status()
response = labrinthapi.json()
for key, value in response.items():
    print(key, ":", value)
#print(urllib.request.urlopen("https://api.modrinth.com/v2/search?query=create_mod"))
#requestapi = urllib.request.urlopen("https://api.modrinth.com/v2/search?query=create_mod")
