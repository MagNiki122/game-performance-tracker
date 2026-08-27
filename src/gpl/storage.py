import csv
import os

def open_csv_writer(filepath):
    file = open(filepath, mode = "a", newline = "")
    writer = csv.writer(file)
    return file, writer

def needs_header(filepath):
    if not os.path.exists(filepath):
        return True
    return os.path.getsize(filepath) == 0

def snapshot_to_row(snapshot):
    return [snapshot.timestamp, snapshot.cpu_percent, snapshot.ram.percent, snapshot.ram.gb,
            snapshot.disk.percent, snapshot.disk.gb, snapshot.gpu.percent, snapshot.gpu.temp]

header = [
    "timestamp",
    "cpu_percent",
    "ram_percent",
    "ram_gb",
    "disk_percent",
    "disk_gb",
    "gpu_percent",
    "gpu_temp"
]
