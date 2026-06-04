import requests
import json
import csv

songs = {
}

release = input("Wat is de discogs releasenummer? ") #example releasenumber = 249504

#api settings
url = "https://api.discogs.com/releases/"+release
apiheaders = {
    "user-agent":"Kobe's School Project"
}
apiparams = {
}

#get data
response = requests.get(url, headers=apiheaders, params=apiparams)
songdata = response.json()
title = songdata["title"]
year = songdata["year"]
artists = songdata["artists"][0]["name"]

#add data to dictionary
songs[release]["title":title]
songs[release]["year":year]
songs[release]["artists":artists]

print(f"Added {title} by {artists} from {year}.")

