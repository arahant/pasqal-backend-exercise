
import random
from typing import Any
from dataclasses import dataclass, field

INSTRUCTIONS_SIZE = 1024

@dataclass
class Job():
    job_id: str
    user_id: str
    program_id: int
    device_type: str

    priority: int = 1
    instructions: Any = field(default_factory=dict)
    result: str = None

    def __init__(self, jid, uid, pid, device_type, prio):
        """
        :type jid: str
        :type uid: str
        :type pid: str
        :type device_type: str
        :type prio: int
        :rtype: None
        """
        self.job_id = jid
        self.user_id = uid
        self.program_id = pid
        self.device_type = device_type
        self.priority = prio
        self.result = None
        self.instructions = Job.get_randomised_instructions()

    @classmethod
    def get_randomised_instructions(cls):
        return random.getrandbits(INSTRUCTIONS_SIZE)

    def serialize(self):
        """ Serializes a Job into a dictionary """
        return {
            "job_id": self.job_id,
            "user_id": self.user_id,
            "program_id": self.program_id,
            "device_type": self.device_type,
            "priority": self.priority
        }


@dataclass
class Program():
    job_id: str
    device_type: str
    priority: int = 1
