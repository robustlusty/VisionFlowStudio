from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
import uuid

from visionflow.project.scene import Scene


@dataclass
class Product:

    name: str

    scenes: List[Scene] = field(default_factory=list)

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_scene(self, scene: Scene):

        self.scenes.append(scene)

    def remove_scene(self, scene: Scene):

        if scene in self.scenes:

            self.scenes.remove(scene)

    def clear(self):

        self.scenes.clear()

    @property
    def duration(self):

        return sum(scene.duration for scene in self.scenes)

    @property
    def scene_count(self):

        return len(self.scenes)

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "scenes": [

                scene.to_dict()

                for scene in self.scenes

            ]

        }

    @classmethod
    def from_dict(cls, data: dict):

        product = cls(

            name=data["name"]

        )

        product.id = data.get("id", product.id)

        for item in data.get("scenes", []):

            product.add_scene(

                Scene.from_dict(item)

            )

        return product

    def __repr__(self):

        return f"<Product {self.name}>"