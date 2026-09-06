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

def frame_times_from_timestamps(timestamps: list[float]) -> list[float]:
    if len(timestamps) < 2:
        return []
    
    results = []
    sorted_timestamps = sorted(timestamps)

    for i in range(1, len(sorted_timestamps)):
        results.append(sorted_timestamps[i] - sorted_timestamps[i - 1])

    return results


def average_fps(frame_times: list[float]) -> float | None:
    if not frame_times:
        return None

    total_time_ms = sum(frame_times)

    if total_time_ms == 0:
        return None

    total_frames = len(frame_times)
    avg_fps = (total_frames * 1000) / total_time_ms

    return avg_fps
    

def print_metrics(cpu_per, mem, disk_mem, gpu, time):
    print(f"\nCurrent Time: {time}")
    print(f"CPU Usage: {cpu_per}%")
    print(f"Ram Usage: {mem.percent}%")
    print(f"Ram GB: {round(mem.gb, 1)}gb")
    print(f"Disk Usage: {disk_mem.percent}%")
    print(f"Disk GB: {round(disk_mem.gb, 1)}gb")
    print(f"GPU Usage: {gpu.percent}%")
    print(f"GPU Temp: {gpu.temp}c")


if __name__ == "__main__":
    # 5 timestamps, each 16.67ms apart (~60 FPS)
    test_timestamps = [0.0, 16.67, 33.34, 50.01, 66.68]

    times = frame_times_from_timestamps(test_timestamps)
    print("Frame times (ms):", times)
    # Expected: [16.67, 16.67, 16.67, 16.67]

    fps = average_fps(times)
    print("Average FPS:", fps)
    # Expected: ~59.98 FPS