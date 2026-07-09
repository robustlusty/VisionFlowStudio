from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QVBoxLayout,QWidget


class StoryboardPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout(self)

        title=QLabel("Storyboard")

        title.setObjectName("PanelTitle")

        preview=QLabel("Storyboard Preview")

        preview.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        layout.addWidget(preview)