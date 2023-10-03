# The code is written by YehorsCode (My name is Yehor) it has the MIT License
# And is FOSS (Fully open source)
# You can use parts of my code in yours code!
# But remember! Mention me and email me (umimc@proton.me) before doing that!
# The code is writen with Python
# You can find Official repositories here:
# | Stable: https://github.com/yehorscode/Umimc
# The code can be incomplete! Email me if you have some ideas or create issue on github if there is a bug

# Importing packages
import tqdm
import requests
from colorama import Fore, Back, Style
import json

# Defining user agent
headerss = {
    'User-Agent': 'yehorscode/Umimc (umimc@proton.me)'
}
# VERY IMPORT VALUES!
debug_mode = False
url_get_findrequest = "https://api.modrinth.com/v2/search?query="
url_get_findrequest_string_type_mod = "&facets=[[%22project_type:mod%22]]"
url_get_findproject = "https://api.modrinth.com/v2/project/"
url_get_project = "https://api.modrinth.com/v2/project/"
fmod_get_projectversion = "https://api.modrinth.com/v2/project/"
fmod_get_projectversion2 = "/version"
# Cdn links not important
fmod_modrinth_cdn1 = "https://cdn.modrinth.com/data/"
fmod_modrinth_cdn2 = "/versions/"
# https://cdn.modrinth.com/data/AANobbMI/versions/mc1.16.3-0.1.0/sodium-fabric-mc1.16.3-0.1.0.jar
# VERY IMPORTANT LISTS/VALUES/DICTIONARIES
fmod_title = {}
fmod_projectid = {}
fmod_categories = {}
fmod_dict = {}
versions_dict = {}
getmod_description = "None"
versions_id_dict = {}

# Stolen from stack overflow
def prettysort(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print(Back.CYAN+"{} ({})".format(item, amount)+Back.RESET)

# Printing Debug Mode Enabled
if debug_mode == True:
    print(Back.WHITE,Fore.BLACK,"Debug mode ENABLED",Fore.RESET,Back.RESET)
    

# Defining what debug text looks like
debug_text = Fore.GREEN + "DEBUG: "

# Welcome text
print(Fore.GREEN + "Welcome to Umimc! Universal Minecraft Mod installer!\n", Fore.RESET)
print(Back.GREEN + "Select your mode:" + Back.RESET)
print(Back.GREEN +
    """
1: Installing, here you can install mods from Modrinth!
2: Remove .minecraft/mods folder (removes all mods)
3: Get info about the mod (requaires project id)
4: Network check (checks is Labrinth avaible)
5: Advanced tools"""+Back.RESET)

# Just a new line
print("\n")

# Input form for user to 
action = input(Back.GREEN+"What do You choose (type here)?: "+Back.RESET)

# Checking what action is action :)
if action == "1":

    # Debug Mode Actions
    if debug_mode == True:
        print(debug_text+"Action 1 was choosed"+Fore.RESET)

    # Choosing the mod
    request_modname = input(Back.GREEN+"What mod You want to Install?: "+ Back.RESET)

    # Requesting Labrinth
    labrinthapi = requests.get(url_get_findrequest + request_modname + url_get_findrequest_string_type_mod , headers=headerss , allow_redirects=True)

    # Debbuging Responses
    if debug_mode == True:
        print(debug_text+"Trying to request Labrinth at: " + url_get_findrequest + request_modname + url_get_findrequest_string_type_mod, Fore.RESET)

    # Returning status code
    if labrinthapi.status_code == 200:
        if debug_mode == True:
            print(debug_text+ "Succesfully requested Labrinth")
    else:
        # Failed request and reason
        print(f"Request failed with status code: {labrinthapi.status_code}")
    response = labrinthapi.json()

    # Just text while waiting...
    print(Fore.CYAN + "Searching throught the response from Labrinth..." + Fore.RESET)

    # Converting Labrinthapi response to json
    jlabrinthapi = labrinthapi.json()
    hits = jlabrinthapi["hits"]
    hits_count = 0

    # Searching entire response
    for mod in hits:
        mod_title = mod["title"]
        mod_id = mod["project_id"]
        fmod_dict[hits_count] = mod_title
        fmod_projectid[hits_count] = mod_id
        hits_count += 1
        if debug_mode == True:
            print(debug_text+"Added "+mod_title+" to fmod_dict"+Fore.RESET)
            print(debug_text+"It's id is: "+mod_id+Fore.RESET)
        
#    print(fmod_dict)

    print(Back.CYAN + "Found "+ str(len(fmod_dict))+" search results"+Back.RESET)
    prettysort(fmod_dict)
    fmod_choose = int(input(Back.GREEN+"What to choose (type a number)?: "+Back.RESET))
    fmod_chosen = 0
    fmod_chosenid = 0
    # Trying to get info from dictionaries
    try:
        fmod_chosen = fmod_dict[fmod_choose]
        fmod_chosenid = fmod_projectid[fmod_choose]
        if debug_mode == True:
            print(debug_text + "Chosen mod is: "+fmod_chosen+"\n"+"Chosen mod project id is: "+fmod_chosenid+Fore.RESET)
    except:
        print(Back.RED+"Invalid argument!"+Back.RESET)
    
    # Getting cdn.modrinth download link
    url_fmod_labrinthapi = fmod_get_projectversion+fmod_chosenid+fmod_get_projectversion2

    fmod_labrinthapi = requests.get(url=fmod_get_projectversion+fmod_chosenid+fmod_get_projectversion2, headers=headerss, allow_redirects=True)

    if debug_mode == True:
        print(debug_text+"Requested labrinth at "+url_fmod_labrinthapi+Fore.RESET)
    if fmod_labrinthapi.status_code == 200:
        if debug_mode == True:
            print(debug_text+"Succesfully accesed Labrinth Api!"+Fore.RESET)
    else:
        print(Back.RED+str(fmod_labrinthapi.status_code)+Back.RESET)
        print(Back.RED+"Something is wrong!"+Back.RESET)

    # Converting to json
    jfmod_labrinthapi = fmod_labrinthapi.json()

    # Description for prettier look
    fmod_desc_labrinthapi = requests.get(url="https://api.modrinth.com/v2/project/"+fmod_chosenid, headers=headerss, allow_redirects=True)
    jfmod_desc_labrinthapi = fmod_desc_labrinthapi.json()
    if debug_mode == True:
        print(debug_text+"Requested labrinth at "+"https://api.modrinth.com/v2/project/"+fmod_chosenid+Fore.RESET)
    if fmod_labrinthapi.status_code == 200:
        if debug_mode == True:
            print(debug_text+"Succesfully accesed Labrinth Api!"+Fore.RESET)
    else:
        print(Back.RED+str(fmod_labrinthapi.status_code)+Back.RESET)
        print(Back.RED+"Something is wrong!"+Back.RESET)
    
    # Printing description
    print(Back.YELLOW+fmod_chosen)
    print(jfmod_desc_labrinthapi["description"])
    print("Followers: "+str(jfmod_desc_labrinthapi["followers"])+Back.RESET)

    # Checking all of the versions
    counterr = 0
    jfmod_desc_labrinthapi["game_versions"]

    for bejba in jfmod_desc_labrinthapi["game_versions"]:
        versions_dict[counterr] = bejba
        counterr += 1
        if debug_mode == True:
            print(debug_text+"Found version: "+bejba+Fore.RESET)
    counterr = 0
    for b in jfmod_desc_labrinthapi["versions"]:
        versions_id_dict[counterr] = b
        counterr +=1
        if debug_mode == True:
            print(debug_text+"Found "+str(len(versions_id_dict))+" versions id's"+Fore.RESET)
            print(b)
    
    # User interaction with fmod (choosing mod id and mod name)
    fmod_user_interaction_modversion = input(Back.GREEN+"What version do You need?: "+Back.RESET)
    
    # Checking if the version is avaible
    counterr = 0
    for i in range(len(versions_dict)):
        if versions_dict[counterr] == fmod_user_interaction_modversion:
            print(Back.GREEN+"Found version!"+Back.RESET)
            break
        else:
            counterr+=1

elif action == "3":
    # Asking for Modrinth Project project id
    project_id = input(Back.CYAN+"What is the project id?: "+Back.RESET)

    # Checking the correctivity of the project ID

    # Correct! ↓
    if len(project_id) == 8:
        print(Back.LIGHTCYAN_EX+"Project id is correct!"+Back.RESET)
        if debug_mode == True:
            print(debug_text+"Project_ID is: "+str(project_id)+Fore.RESET)
        labrinthapi_project_info = requests.get(url=url_get_findproject+project_id,headers=headerss,allow_redirects=True)
        print(labrinthapi_project_info)

    # Incorrect! ↓
    else:
        print(Back.RED+"It seems that you entered wrong id!"+Back.RESET)
        print(Back.RED+"If you think this is an issue create a bug report here: https://github.com/yehorscode/Umimc/issues/new"+Back.RESET)


elif action == "4":
    # Fetching (geting statisticks)
    url_labrinthapi_statistics = "https://api.modrinth.com/v2/statistics"
    labrinthapi_statistics = requests.get(url_labrinthapi_statistics, allow_redirects=True,headers=headerss)
    if labrinthapi_statistics.status_code == 200:
        if debug_mode == True:
            print(debug_text+"Succesfully requested "+url_labrinthapi_statistics)
        print(Back.LIGHTMAGENTA_EX+"Labrinth is working succesfuly!\nHere you can check Modrinth's status: https://status.modrinth.com/"+Back.RESET)
    else:
        print(Back.LIGHTMAGENTA_EX+"Labrinth is NOT working succesfuly :( You are unable to install Mods!\nHere you can check Modrinth's status: https://status.modrinth.com/"+Back.RESET)


elif action == "5":
    # Debug mode choosing
    print(Back.GREEN + """1: Debug Mode, current state: """+str(debug_mode)+Back.RESET)
    # Choosing
    action_advanced_actions_choose = input(Back.GREEN+"What to choose (type here): "+Back.RESET)
    print("\n")
    # Choosing action
    if action_advanced_actions_choose == "1":
        if debug_mode == True:
            debug_mode = False
            print(debug_text+"Turned OFF debugging "+str(debug_mode)+Fore.RESET)
        elif debug_mode == False:
            debug_mode = True
            print(debug_text+"Turned ON debugging "+str(debug_mode)+Fore.RESET)


else:
    print(Back.YELLOW + "Hmmm I do not understand! Could you restart me?"+Back.RESET)