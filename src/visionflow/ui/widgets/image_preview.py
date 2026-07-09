from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QVBoxLayout,QWidget


class ImagePreview(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout(self)

        title=QLabel("Image Preview")

        title.setObjectName("PanelTitle")

        image=QLabel("No Image")

        image.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        layout.addWidget(image)