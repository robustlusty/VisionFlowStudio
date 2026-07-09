from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from datetime import datetime
import uuid

from visionflow.project.product import Product


@dataclass
class Project:

    name: str

    products: List[Product] = field(default_factory=list)

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime = field(default_factory=datetime.now)

    updated_at: datetime = field(default_factory=datetime.now)

    favorite: bool = False

    def add_product(self, product: Product):

        self.products.append(product)

        self.touch()

    def remove_product(self, product: Product):

        if product in self.products:

            self.products.remove(product)

            self.touch()

    def clear(self):

        self.products.clear()

        self.touch()

    @property
    def product_count(self):

        return len(self.products)

    @property
    def scene_count(self):

        return sum(

            product.scene_count

            for product in self.products

        )

    @property
    def duration(self):

        return sum(

            product.duration

            for product in self.products

        )

    def touch(self):

        self.updated_at = datetime.now()

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "favorite": self.favorite,

            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

            "products": [

                product.to_dict()

                for product in self.products

            ]

        }

    @classmethod
    def from_dict(cls, data: dict):

        project = cls(

            name=data["name"]

        )

        project.id = data.get("id", project.id)

        project.favorite = data.get("favorite", False)

        created = data.get("created_at")

        updated = data.get("updated_at")

        if created:

            project.created_at = datetime.fromisoformat(created)

        if updated:

            project.updated_at = datetime.fromisoformat(updated)

        for item in data.get("products", []):

            project.add_product(

                Product.from_dict(item)

            )

        return project

    def __repr__(self):

        return f"<Project {self.name}>"