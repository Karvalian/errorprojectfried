import requests
from bs4 import BeautifulSoup
from colorama import * 
import os

def scan(url,full):
    print(Fore.RED+"[!] s-sql : SQL Vuln Scanner [!]")
    print(Fore.BLACK+"[!] Target URL : {url}")
    print(Fore.BLACK+"[!] Full Scan  : {full}")
    print(" ")
    if(full==True):
        req = requests.get(url).text
        soup = BeautifulSoup(req.text, 'html.parser')
        for link in soup.find_all('a'):
            suburl = link.get('href')
            req1 = requests.get(suburl+"'")
            sql = "SQL"
            found = req1.find(sql)
            if(found):
                print(Fore.GREEN+f"[+] Vuln Found! URL : {suburl}+'")
    
    elif(full==False):
        found = 0
        req = requests.get(url+"'").text 
        found = req.find("SQL")
        if(found>0):
            print(Fore.GREEN+f"[+] Vuln Found! URL : {url}+'")


scan("https://samaritermuensingen.ch/index.php?id=2",False)
