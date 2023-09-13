import webbrowser
import requests
from colorama import Fore, Back, Style

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}


print(Fore.MAGENTA + "Welcome to Unimc! Universal Minecraft Mod installer!", Fore.RESET)
print(Back.CYAN + "Select your mode:" + Back.RESET)
print(Back.CYAN +
    """
1: Installing, here you can install mods from Modrinth!
2: Remove .minecraft/mods folder (removes all mods)"""+Back.RESET)

print(requests.get("https://api.modrinth.com/v2/query=fabric"))