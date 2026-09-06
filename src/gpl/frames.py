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

if __name__ == "__main__":
    # 5 timestamps, each 16.67ms apart (~60 FPS)
    test_timestamps = [0.0, 16.67, 33.34, 50.01, 66.68]

    times = frame_times_from_timestamps(test_timestamps)
    print("Frame times (ms):", times)
    # Expected: [16.67, 16.67, 16.67, 16.67]

    fps = average_fps(times)
    print("Average FPS:", fps)
    # Expected: ~59.98 FPS