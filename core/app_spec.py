from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime


@dataclass
class AppSpec:
    app_id: str
    name: str
    goal: str
    features: List[str]
    constraints: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )
    status: str = "draft"

    def to_dict(self):
        return {
            "app_id": self.app_id,
            "name": self.name,
            "goal": self.goal,
            "features": self.features,
            "constraints": self.constraints,
            "created_at": self.created_at,
            "status": self.status,
        }
