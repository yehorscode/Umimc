# Umimc AutoInstaller
# This app helps you install Umimc!
# You need os (library) which is already installed!
# If You have noticed bugs, email me:
# umimc@proton.me

# Importing libraries
import os

print("Welcome! You are starting Umimc AutoInstall!")
print("Follow the instructions to complete the installation\n")
print("\033[1m" + """Choose an option:
1. Install Umimc
2. Close the app""" + "\033[0m")

action_start = input("What do You choose? (1/2): ")

print("Thank You!")
print("One more question,\n")
print("What os do You have?")
action_os = input("\033[1m" + "Choose the os: (Windows (W), Linux(L), Mac Os(M) Type W, L or M)" + "\033[0m")

if action_start.lower() == "w" or action_start.lower() == "windows" or action_start.lower() == "win":
    print(f"""WARNING!
{action_os} this os is NOT officially suported for now.
If You think this is a bug email me: umimc@proton.me""")
    action_oserror = input("Do You want to continue? (Y (Yes), N (No))")
    user_os = "win"
elif action_start.lower() == "l" or action_start.lower() == "linux" or action_start.lower() == "lin":
    print()
    user_os = "lin"
if action_start.lower() == "m" or action_start.lower() == "mac os" or action_start.lower() == "mac":
    print(f"""WARNING!
{action_os} this os is NOT officially suported for now.
If You think this is a bug email me: umimc@proton.me""")
    action_oserror = input("Do You want to continue? (Y (Yes), N (No))")
    user_os = "mac"

def debug(text):
    print("\033[1m" + text + "\033[0m")

if action_oserror.lower() == "y" or action_oserror.lower() == "yes":
    print()
else:
    print("Bye!")
    quit()

if user_os == "lin":
    os.system("cd ~")
    debug("Executed cd ~")
    os.system("mkdir Umimc")
    debug("Executed mkdir Umimc")
    debug("Umimc folder was made in Your's home directory")
    os.system("cd Umimc")
    debug("Going to the Umimc folder (cd Umimc)")
    os.system("curl -LJO https://github.com/yehorscode/Umimc/releases/latest")
    debug("Downloaded repo")
    