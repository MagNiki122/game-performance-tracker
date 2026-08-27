import psutil
from models import DiskInfo, RamInfo

cpu_warm_up = psutil.cpu_percent(interval = 0.1)
def get_cpu_usage():
    cpu_per = psutil.cpu_percent(interval = None)
    if cpu_per == 0.0:
        cpu_per = cpu_warm_up
    return cpu_per

def get_disk_usage(path = "C:/"):
    disk_info = psutil.disk_usage(path)

    disk = DiskInfo(
        percent = disk_info.percent,
        gb = round(disk_info.total / (1024**3),1)
    )
    return disk

def get_memory_usage():
    ram_info = psutil.virtual_memory()
    ram = RamInfo(
        percent = ram_info.percent,
        gb = round(ram_info.total / (1024**3),1)
    )
    return ram

def print_metrics(cpu_per, mem, disk_mem, gpu, time):
    print(f"\nCurrent Time: {time}")
    print(f"CPU Usage: {cpu_per}%")
    print(f"Ram Usage: {mem.percent}%")
    print(f"Ram GB: {round(mem.gb, 1)}gb")
    print(f"Disk Usage: {disk_mem.percent}%")
    print(f"Disk GB: {round(disk_mem.gb, 1)}gb")
    print(f"GPU Usage: {gpu.percent}%")
    print(f"GPU Temp: {gpu.temp}c")
     



