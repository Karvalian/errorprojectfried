import requests
url = input("URL : ")
"""https://samaritermuensingen.ch/index.php?id=2"""
s = str(url+"'")
u = requests.get(url).text.count('SQL')
if(u):
    print("Vuln Found!")
else:
    print("Vuln Not Found!")
