import sqlite3
def snapshot_to_row(snapshot):
    return [snapshot.timestamp, snapshot.cpu_percent, snapshot.ram.percent, snapshot.ram.gb,
            snapshot.disk.percent, snapshot.disk.gb, snapshot.gpu.percent, snapshot.gpu.temp]


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
    cursor.execute(
        "INSERT INTO snapshots (timestamp, cpu_percent, ram_percent, ram_gb, disk_percent, disk_gb, gpu_percent, gpu_temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        row
    )
    connection.commit()