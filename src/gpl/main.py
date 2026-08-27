from metrics import get_cpu_usage, get_disk_usage, get_memory_usage, print_metrics
from models import Snapshot, GPUInfo
import time
from datetime import datetime

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
        print_metrics(snapshot.cpu_percent, snapshot.ram, snapshot.disk, snapshot.gpu, snapshot.timestamp)
        time.sleep(1)
    except KeyboardInterrupt as keyInterrupt:
        print("Ending program")
        break







