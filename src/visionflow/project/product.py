from dataclasses import dataclass, field


@dataclass
class Product:

    name: str

    images: list = field(default_factory=list)

    prompts: list = field(default_factory=list)

    videos: list = field(default_factory=list)