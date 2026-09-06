import psutil
import time
import json
import os

KNOWN_GAMES = []
base_dir = os.path.dirname(os.path.abspath(__file__))
game_dir = os.path.join(base_dir, "games.json")

with open(game_dir, "r", encoding = "utf-8") as file:
    data = json.load(file)

KNOWN_GAMES = data["applications"]

def find_running_game(known_games):
    lower_case = [item.lower() for item in known_games]

    for proc in psutil.process_iter(['pid', 'name']):
        proc_name = str.lower(proc.info['name'])
        if (proc_name in lower_case):
            return proc.info['name']
    return None 

def wait_for_game(known_games):
    print("Waiting For Game...")
    game_name = find_running_game(known_games)
    while game_name is None:
        time.sleep(3)
        game_name = find_running_game(known_games)
    return game_name
