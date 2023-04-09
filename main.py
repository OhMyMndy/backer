import os
import sys
import requests
import json
import deemix
import deemix.utils.localpaths as localpaths
import spleet

user_id = sys.argv[1]
api_url = f'https://api.deezer.com/user/{user_id}/playlists'

deezer_arl = sys.argv[2]
if not os.path.exists(localpaths.getConfigFolder()):
    os.mkdir(localpaths.getConfigFolder())

arl_path = localpaths.getConfigFolder() / '.arl'

f = open(arl_path, "w")
f.write(deezer_arl)
f.close()

search_term = sys.argv[3]

def get_playlists():
    playlists = []
    url = api_url
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)

            filtered = [p for p in data["data"] if search_term in p["title"]]
            playlists = playlists + filtered

            if "next" in data:
                url = data["next"]
            else:
                break

    return playlists


class Listener:
    @classmethod
    def send(cls, key, value=None):
        # print(key, value)
        if key == 'updateQueue' and "downloaded" in value and value["downloaded"] == True:
            downloaded_files.append(value["downloadPath"])


for playlist in get_playlists():
    print(f'Downloading {playlist["title"]}')
    downloaded_files = []
    deemix.download([playlist["link"]], None, True, None, Listener)

    spleet.spleet(files)
