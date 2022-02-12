from typing import Optional

from pydantic.dataclasses import dataclass


__all__ = [
    'Message',
    'ReceivedMessage',
    'RedirectedMessage',
]


@dataclass
class Message:
    text: str


@dataclass
class ReceivedMessage:
    from_id: str
    name: str
    text: str


@dataclass
class RedirectedMessage:
    received_message: ReceivedMessage
    destination_message: Optional[Message] = None
