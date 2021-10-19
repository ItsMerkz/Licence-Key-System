import requests

licen = input("Licence Code")

resp = requests.get("").text # put website there, pastebin or your own 

resp = resp.splitlines()


if licen in resp:
    print("Licence accepted!")
    access = True
else:
    print("Licence is incorrect!")
    access = False

if access == True:
"""
Put your code here 
"""
