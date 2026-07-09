from pathlib import Path


class ImageStore:

    def __init__(self):
        self.images = []

    def clear(self):
        self.images.clear()

    def add(self, file):
        path = Path(file)

        if path.exists():
            self.images.append(path)

    def addMany(self, files):

        for file in files:
            self.add(file)

    def all(self):
        return self.images