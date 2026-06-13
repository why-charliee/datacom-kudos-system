from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict
import uuid


@dataclass
class Kudos:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sender_id: Any = None
    recipient_id: Any = None
    message: str = ""
    is_visible: bool = True
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + 'Z')

    def __post_init__(self) -> None:
        if not isinstance(self.message, str) or not self.message.strip():
            raise ValueError("`message` must be a non-empty string")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Kudos":
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            sender_id=data.get("sender_id"),
            recipient_id=data.get("recipient_id"),
            message=data.get("message", ""),
            is_visible=data.get("is_visible", True),
            created_at=data.get("created_at", datetime.utcnow().isoformat() + 'Z'),
        )