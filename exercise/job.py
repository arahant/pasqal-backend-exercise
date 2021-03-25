from typing import Any
from dataclasses import dataclass, field


@dataclass
class Job():
    id: str
    user_id: str
    device_type: str
    program_id: int

    priority: int = 1
    instructions: Any = field(default_factory=dict)
    result: str = None


@dataclass
class Program():
    id: str
    device_type: str
    priority: int = 1
