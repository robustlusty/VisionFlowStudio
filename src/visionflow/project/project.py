from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Project:

    name: str = "Untitled"

    root: Path | None = None

    products: list = field(default_factory=list)

    settings: dict = field(default_factory=dict)