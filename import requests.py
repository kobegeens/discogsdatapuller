import requests
import json
import csv

songs = {
}

#api settings
apiheaders = {
    "user-agent":"Kobe's School Project"
}
apiparams = {
}
filename = "songs.csv"


def add_song():
    #get data
    release = input("discogs releasenumber: ") #example releasenumber = 249504
    url = "https://api.discogs.com/releases/"+release
    try:
        response = requests.get(url, headers=apiheaders, params=apiparams)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(response)
        print("Song unavailable or bad internet connection.")
        start()
    songdata = response.json()
    ##print(songdata)
    title = songdata["title"]
    artists = songdata["artists"][0]["name"]
    year = songdata["year"]

    #add data to dictionary
    songs[release] = {"title":title, "year":year, "artists":artists}


    print(f"Added {title} by {artists} from {year}.")

    #CSV
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                print(row[0])
                if row[0] == release:
                    print("song already added")
                    start()
                else:
                    continue
    with open(filename, "a", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([release] + list(songs[release].values()))
    start()

def delete_song():
    delete = input("discogs releasenumber: ")
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        currentrows = [row for row in reader if row]
    keeprows = [row for row in currentrows if row and row[0] != delete]
    if len(currentrows) == len(keeprows):
            print("couldn't find song")
            start()
    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(keeprows)
    print("succesfully deleted song")
    start()


def list_songs():
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                print(f"{row[0]} {row[1]} by {row[2]} from {row[3]}")
    start()

def start():
    #interface
    choice = input("\n0: add song \n1: delete song \n3: list songs\n4: exit\n")
    match choice:
        case "0":
            add_song()
        case "1":
            delete_song()
        case "3":
            list_songs()
        case "4":
            exit()

start()