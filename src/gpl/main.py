from metrics import get_cpu_usage, get_disk_usage, get_memory_usage, print_metrics
from models import Snapshot, GPUInfo
from detection import find_running_game, wait_for_game, KNOWN_GAMES
import database
import time
from datetime import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "session.db")

def run_application(connection):
    while True:
        if find_running_game(KNOWN_GAMES) is None:
            print("Application Closed")
            break
        timestamp = datetime.now().strftime("%H:%M:%S") 
        cpu_per = get_cpu_usage()
        ram_info = get_memory_usage()
        disk_info = get_disk_usage('C:/')
        gpu_info = GPUInfo(available=False,percent=None,temp=None)
        snapshot = Snapshot(
            timestamp = timestamp,
            cpu_percent = cpu_per,
            ram = ram_info,
            disk = disk_info,
            gpu = gpu_info
            )
        database.insert_snapshot(connection, snapshot)
        print_metrics(snapshot.cpu_percent, snapshot.ram, snapshot.disk, snapshot.gpu, snapshot.timestamp)
        time.sleep(1)

try:
    while True:
        connection = database.get_connection(db_path)
        database.create_table(connection)
        game_name = wait_for_game(KNOWN_GAMES)
        print(f"Game Detected: {game_name}")
        print("Starting Performance Section...")
        run_application(connection)

except KeyboardInterrupt as keyInterrupt:
    connection.close()
    print("Ending Program")
    
    