from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Prompt:

    title: str

    content: str = ""

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime = field(default_factory=datetime.now)

    updated_at: datetime = field(default_factory=datetime.now)

    tags: list[str] = field(default_factory=list)

    favorite: bool = False

    def rename(self, title: str):

        self.title = title

        self.updated_at = datetime.now()

    def set_content(self, content: str):

        self.content = content

        self.updated_at = datetime.now()

    def add_tag(self, tag: str):

        if tag not in self.tags:

            self.tags.append(tag)

    def remove_tag(self, tag: str):

        if tag in self.tags:

            self.tags.remove(tag)

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "content": self.content,

            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

            "tags": self.tags,

            "favorite": self.favorite,

        }

    @classmethod
    def from_dict(cls, data: dict):

        prompt = cls(

            title=data["title"],

            content=data.get("content", "")

        )

        prompt.id = data.get("id", prompt.id)

        prompt.tags = data.get("tags", [])

        prompt.favorite = data.get("favorite", False)

        created = data.get("created_at")

        updated = data.get("updated_at")

        if created:

            prompt.created_at = datetime.fromisoformat(created)

        if updated:

            prompt.updated_at = datetime.fromisoformat(updated)

        return prompt

    def __repr__(self):

        return f"<Prompt {self.title}>"