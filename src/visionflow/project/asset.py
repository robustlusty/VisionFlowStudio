from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from typing import Any
import uuid


@dataclass
class Asset:
    """
    Base asset object.

    Every file inside VisionFlow Studio
    (image, video, audio, prompt export...)
    is represented by an Asset.
    """

    path: Path

    asset_type: str = "file"

    name: str = ""

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime = field(default_factory=datetime.now)

    metadata: dict[str, Any] = field(default_factory=dict)

    tags: list[str] = field(default_factory=list)

    favorite: bool = False

    def __post_init__(self):

        self.path = Path(self.path)

        if not self.name:

            self.name = self.path.name

    @property
    def exists(self) -> bool:

        return self.path.exists()

    @property
    def extension(self) -> str:

        return self.path.suffix.lower()

    @property
    def parent(self) -> Path:

        return self.path.parent

    def rename(self, new_name: str):

        self.name = new_name

    def add_tag(self, tag: str):

        if tag not in self.tags:

            self.tags.append(tag)

    def remove_tag(self, tag: str):

        if tag in self.tags:

            self.tags.remove(tag)

    def set_metadata(self, key: str, value: Any):

        self.metadata[key] = value

    def get_metadata(self, key: str, default=None):

        return self.metadata.get(key, default)

    def to_dict(self) -> dict:

        return {

            "id": self.id,

            "name": self.name,

            "path": str(self.path),

            "asset_type": self.asset_type,

            "created_at": self.created_at.isoformat(),

            "metadata": self.metadata,

            "tags": self.tags,

            "favorite": self.favorite,

        }

    @classmethod
    def from_dict(cls, data: dict):

        asset = cls(

            path=Path(data["path"]),

            asset_type=data.get("asset_type", "file"),

            name=data.get("name", ""),

        )

        asset.id = data.get("id", asset.id)

        asset.metadata = data.get("metadata", {})

        asset.tags = data.get("tags", [])

        asset.favorite = data.get("favorite", False)

        created = data.get("created_at")

        if created:

            asset.created_at = datetime.fromisoformat(created)

        return asset

    def __str__(self):

        return self.name

    def __repr__(self):

        return f"<Asset {self.name}>"