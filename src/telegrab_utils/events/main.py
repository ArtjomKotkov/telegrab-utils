from typing import Iterable

from pydantic.dataclasses import dataclass

from .base import BaseEvent

from ..messages import Message, RedirectedMessage


__all__ = [
    'ConnectEvent',
    'DisconnectEvent',
    'SendRedirectedMessageToOwnerEvent',
    'SendServiceMessage',
]


@dataclass
class ConnectEvent(BaseEvent):
    bot_id: str


@dataclass
class DisconnectEvent(BaseEvent):
    bot_id: str


@dataclass
class SendRedirectedMessageToOwnerEvent(BaseEvent):
    bot_ids: Iterable[str]
    message: RedirectedMessage


@dataclass
class SendServiceMessage(BaseEvent):
    destination_ids: Iterable[str]
    message: Message
