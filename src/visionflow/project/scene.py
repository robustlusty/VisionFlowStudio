from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
import uuid

from visionflow.project.prompt import Prompt


@dataclass
class Scene:
    """
    Một scene trong storyboard.
    """

    title: str

    duration: float = 8.0

    prompts: List[Prompt] = field(default_factory=list)

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_prompt(self, prompt: Prompt):

        self.prompts.append(prompt)

    def remove_prompt(self, prompt: Prompt):

        if prompt in self.prompts:

            self.prompts.remove(prompt)

    def clear(self):

        self.prompts.clear()

    @property
    def prompt_count(self):

        return len(self.prompts)

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "duration": self.duration,

            "prompts": [

                p.to_dict()

                for p in self.prompts

            ]

        }

    @classmethod
    def from_dict(cls, data: dict):

        scene = cls(

            title=data["title"],

            duration=data.get("duration", 8.0)

        )

        scene.id = data.get("id", scene.id)

        for item in data.get("prompts", []):

            scene.add_prompt(

                Prompt.from_dict(item)

            )

        return scene

    def __repr__(self):

        return f"<Scene {self.title}>"