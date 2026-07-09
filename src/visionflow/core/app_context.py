from visionflow.core.image_store import ImageStore


class AppContext:

    def __init__(self):
        self.images = ImageStore()


app = AppContext()