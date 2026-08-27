from dataclasses import dataclass
from datetime import datetime

@dataclass
class RamInfo:
    percent: float
    gb: float

@dataclass
class DiskInfo:
    percent: float
    gb: float

@dataclass
class GPUInfo:
    available: bool = False
    percent: float | None = None
    temp: float | None = None

@dataclass
class Snapshot:
    timestamp: datetime
    cpu_percent: float
    ram: RamInfo
    disk: DiskInfo
    gpu: GPUInfo