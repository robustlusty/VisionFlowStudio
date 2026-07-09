from dataclasses import dataclass
from pathlib import Path


@dataclass
class Asset:

    path: Path

    type: str