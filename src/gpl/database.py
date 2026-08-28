import sqlite3
from storage import snapshot_to_row
from models import Snapshot, RamInfo, DiskInfo, GPUInfo
from datetime import datetime


def get_connection(db_path):
    connection = sqlite3.connect(db_path)
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS snapshots (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            cpu_percent REAL,
            ram_percent REAL,
            ram_gb REAL,
            disk_percent REAL,
            disk_gb REAL,
            gpu_percent REAL,
            gpu_temp REAL
        )
        """
    )
    connection.commit()
    
def insert_snapshot(connection, snapshot):
    cursor = connection.cursor()
    row = snapshot_to_row(snapshot)
    print("Row to insert:", row)
    cursor.execute(
        "INSERT INTO snapshots (timestamp, cpu_percent, ram_percent, ram_gb, disk_percent, disk_gb, gpu_percent, gpu_temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        row
    )
    print("Rows affected:", cursor.rowcount)
    connection.commit()
    print("Committed.")


con = get_connection("session.db")
create_table(con)

test_snapshot = Snapshot(
    timestamp=datetime.now().strftime("%H:%M:%S"),
    cpu_percent=15.5,
    ram=RamInfo(percent=60.0, gb=15.6),
    disk=DiskInfo(percent=20.5, gb=952.5),
    gpu=GPUInfo(available=False, percent=None, temp=None)
)

insert_snapshot(con, test_snapshot)
