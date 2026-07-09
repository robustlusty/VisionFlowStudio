from dataclasses import dataclass


@dataclass
class Scene:

    image: str = ""

    prompt: str = ""

    duration: float = 8.0