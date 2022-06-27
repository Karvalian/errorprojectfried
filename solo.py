from colorama import *
import os
from time import *
import optparse
import random

def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "█" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

def load():
    for i in range(101):
        progress(i)
        sleep(0.01)

class console:
    c1 = Fore.RED+"solo > "
    c2 = Fore.RED+"[root|solo]: "

#class banner:

class banner:
    info = [Fore.BLUE+"""
    - For SQL Vuln Scanner : 
        " s-sql start "
        " set url example "
        " set full true "
        " start s-sql"
    """]
    banner = ["""
 _________________________________________________________________
< Hello! Welcome to SOLO console... (Educational purposes only :))>
 -----------------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
    ""","""
     _______  _______  ___      _______ 
    |       ||       ||   |    |       |
    |  _____||   _   ||   |    |   _   |
    | |_____ |  | |  ||   |    |  | |  |
    |_____  ||  |_|  ||   |___ |  |_|  |
    _____|  ||       ||       ||       |
    |_______||_______||_______||_______|
    ""","""
    ──────────────────────────────────
    ─────────▄▄───────────────────▄▄──
    ──────────▀█───────────────────▀█─
    ──────────▄█───────────────────▄█─
    ──█████████▀───────────█████████▀─
    ───▄██████▄─────────────▄██████▄──
    ─▄██▀────▀██▄─────────▄██▀────▀██▄
    ─██────────██─────────██────────██
    ─██───██───██─────────██───██───██
    ─██────────██─────────██────────██
    ──██▄────▄██───────────██▄────▄██─
    ───▀██████▀─────────────▀██████▀──
    ──────────────────────────────────
    ──────────────────────────────────
    ──────────────────────────────────
    ───────────█████████████──────────
    ──────────────────────────────────
    ──────────────────────────────────
    """]
class info:
    commands = """
    For SQL Vuln Scanner :
        
        s-sql start
        set url example
        set full True
        start s-sql

    Ping URL :

        ping url
    
    Restart Program :

        restart or reboot

    """

if __name__  ==  "__main__":
    os.system("cls")
    print(random.choice(banner.banner))
    print(random.choice(banner.info))
    load()
    while(True):
        seturl = "set url "
        fulls = "set full "
        ping = "ping "
        print("\n")
        cmd = input(Fore.BLACK+console.c1)
        print(Fore.BLUE+"")
        
        if(cmd=="s-sql start"):
            os.system("python3 ./s-sql/main.py")

        elif(ping in cmd):
            url = cmd.replace("ping","")
            os.system(f"ping {url}")

        elif(cmd=="show commands" or cmd=="help"):
            print(info.commands)
        
        elif(cmd=="restart" or cmd=="reboot"):
            os.system("sudo python3 solo.py")

        elif(cmd=="clear" or cmd =="cls"):
            os.system("cls")
        
        else:
            print("[!] Warning : Command Error! Please retry working command. For commands input 'show commands'")