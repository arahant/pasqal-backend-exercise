
import random
from typing import Any
from dataclasses import dataclass, field

INSTRUCTIONS_SIZE = 1024

@dataclass
class Job():
    id: str
    user_id: str
    program_id: int
    device_type: str

    priority: int = 1
    instructions: Any = field(default_factory=dict)
    result: str = None

    def __init__(self, jid, uid, pid, type, prio):
        """
        :type jid: str
        :type uid: str
        :type pid: str
        :type type: str
        :type prio: int
        :rtype: None
        """
        self.id = jid
        self.user_id = uid
        self.program_id = pid
        self.device_type = type
        self.priority = prio
        self.result = None
        self.instructions = Job.get_randomised_instructions()

    @classmethod
    def get_randomised_instructions(cls):
        return random.getrandbits(INSTRUCTIONS_SIZE)

    def serialize(self):
        """ Serializes a Job into a dictionary """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "program_id": self.program_id,
            "type": self.device_type,
            "priority": self.priority
        }


@dataclass
class Program():
    id: str
    device_type: str
    priority: int = 1
