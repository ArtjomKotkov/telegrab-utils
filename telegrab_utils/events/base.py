from dataclasses import asdict
from typing import Mapping, Any

from pydantic.dataclasses import dataclass

from ..strings import title_case_to_camel_case


@dataclass
class BaseEvent:

    @classmethod
    def from_dict(cls, event_data: Mapping[str, Any]):
        return cls(**event_data)

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)

    @classmethod
    @property
    def type(cls) -> str:
        return title_case_to_camel_case(cls.__name__)
