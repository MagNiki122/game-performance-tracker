from metrics import get_cpu_usage, get_disk_usage, get_memory_usage, print_metrics
from models import Snapshot, GPUInfo
from detection import find_running_game, wait_for_game, KNOWN_GAMES
import storage
import time
from datetime import datetime
import csv

filepath = "session.csv"

def run_application():
    while True:
        try:
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
            snapshot_row = storage.snapshot_to_row(snapshot)
            writer.writerow(snapshot_row)
            print_metrics(snapshot.cpu_percent, snapshot.ram, snapshot.disk, snapshot.gpu, snapshot.timestamp)
            time.sleep(1)
        except KeyboardInterrupt as keyInterrupt:
            file.close()
            print("Ending program")
            break


game_name = wait_for_game(KNOWN_GAMES)
print(f"Game Detected: {game_name}")
print("Starting Performance Section...")

needs_header = storage.needs_header(filepath)
file, writer = storage.open_csv_writer(filepath)
if needs_header:
    writer.writerow(storage.header)
run_application()