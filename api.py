import requests

#this worked yay :D

response = requests.get("http://api.github.com")
if response.status_code == 200 :
    print("AWESOME!")
elif response.status_code == 404 :
    print("Not Found!")
else:
   print("ERROR!")