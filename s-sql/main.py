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

class scan:
    url = "google.com"
    full = False

if __name__  ==  "__main__":
    os.system("cls")
    print(Fore.BLACK)
    print(random.choice(banner.banner))
    print(random.choice(banner.info))
    load()
    print("")
    print(Fore.GREEN+"\n[!] s-sql started!")
    Turn = True
    while(Turn):
        seturl = "set url "
        fulls = "set full "
        ping = "ping "
        print("\n")
        cmd = input(console.c1)
        print(Fore.BLUE+"")
        
        if(seturl in cmd):
            s = cmd.replace("set url ","")
            scan.url = s
            print(Fore.GREEN+f"[!] INFO : Target {Fore.BLUE}URL{Fore.GREEN} setted as : {Fore.RED}{scan.url}")    
        
        elif(fulls in cmd):
            s = cmd.replace("set full ","")
            scan.url = s
            print(Fore.GREEN+f"[!] INFO : Full {Fore.BLUE}sql vuln scan{Fore.GREEN} option setted as : {Fore.RED}{scan.full}")    

        elif(cmd == "start s-sql"):
            print("\n[!!] Starting SQL Vulnerable Scanner....\n")
            load()
            os.system("python3 ./s-sql/start.py")

        elif(ping in cmd):
            url = cmd.replace("ping ","")
            os.system(f"ping {url}")

        elif(cmd=="show commands" or cmd=="help"):
            print(info.commands)

        elif(cmd=="restart" or cmd=="reboot"):
            os.system("sudo python3 solo.py")
            
        else:
            print("[!] Warning : Command Error! Please retry working command. For commands input 'show commands'")