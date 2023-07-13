import lyricsgenius
#import pprint
from urllib.error import HTTPError
import os

pp = pprint.PrettyPrinter(indent=2)

genius = lyricsgenius.Genius(os.environ.get("GENIUS_TOKEN"))
#genius.response_format = "markdown"
genius.verbose = True

quit_app = False

open_text = """
      ___           ___           ___                       ___           ___     
     /\  \         /\  \         /\__\          ___        /\__\         /\  \    
    /::\  \       /::\  \       /::|  |        /\  \      /:/  /        /::\  \   
   /:/\:\  \     /:/\:\  \     /:|:|  |        \:\  \    /:/  /        /:/\ \  \  
  /:/  \:\  \   /::\~\:\  \   /:/|:|  |__      /::\__\  /:/  /  ___   _\:\~\ \  \ 
 /:/__/_\:\__\ /:/\:\ \:\__\ /:/ |:| /\__\  __/:/\/__/ /:/__/  /\__\ /\ \:\ \ \__\ 
 \:\  /\ \/__/ \:\~\:\ \/__/ \/__|:|/:/  / /\/:/  /    \:\  \ /:/  / \:\ \:\ \/__/
  \:\ \:\__\    \:\ \:\__\       |:/:/  /  \::/__/      \:\  /:/  /   \:\ \:\__\  
   \:\/:/  /     \:\ \/__/       |::/  /    \:\__\       \:\/:/  /     \:\/:/  /  
    \::/  /       \:\__\         /:/  /      \/__/        \::/  /       \::/  /   
     \/__/         \/__/         \/__/                     \/__/         \/__/    

Search syntax:

[search type];[search terms]


"""

search_results = []

def song_cli():
    song_num_input = input("Please enter the song you would like to view the lyrics of: ")
    #print(search_results[song_num])
    song_num = -1
    while song_num == -1
        try:
            song_num = int(song_num_input)
        except ValueError:
            print("invalid input!")
            song_num_input = input("Please enter the song you would like to view the lyrics of: ")
    try:
        song = genius.lyrics(search_results[song_num]["result"]["id"])
        print("\n====================")
        print(search_results[song_num]["result"]["full_title"])
        print("====================\n")
        for line in song.splitlines():
            if song.index(line) == 0 and not line == "":
                print(line.split("Lyrics")[1])
                continue
            print(line)
        print("\n====================\n")
    except HTTPError as e:
        print(e.errno)
        print(e.args[0])
        print(e.args[1])
    #except Timeout:
    #    print("timeout")



def print_song_search_reults():
    print(" === SONGS ===")
    for result in range(len(search_results)):
        song = search_results[result]["result"]
        print("{0}. {1}".format(result, song["full_title"]))
    song_cli()


def search_song(song: str):
    for i in range(3):
        search_results.extend(genius.search_songs(song, None, i)["hits"])
    #pp.pprint(search_results)
    print_song_search_reults()
    #pp.pprint(search_results)


def cli():
    search_results.clear()
    first_in = input("Please input your search command: ")
    print(first_in)
    if first_in[0] == "q":
        quit_app = True
        return False
    
    args = first_in.split(";")

    match args[0]:
        case "song":
            search_song(args[1])
    return True
    

print(open_text)
while True:
    a = cli()
    if a == False:
        break
