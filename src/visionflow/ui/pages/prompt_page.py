from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QSplitter,
    QVBoxLayout,
)

from visionflow.ui.widgets.prompt_editor import PromptEditor
from visionflow.ui.widgets.storyboard_panel import StoryboardPanel
from visionflow.ui.widgets.image_preview import ImagePreview
from visionflow.ui.widgets.batch_queue import BatchQueue


class PromptPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        root = QSplitter(Qt.Horizontal)

        left = QSplitter(Qt.Vertical)
        right = QSplitter(Qt.Vertical)

        left.addWidget(PromptEditor())
        left.addWidget(ImagePreview())

        right.addWidget(StoryboardPanel())
        right.addWidget(BatchQueue())

        left.setSizes([500, 300])
        right.setSizes([350, 450])

        root.addWidget(left)
        root.addWidget(right)

        root.setSizes([900, 500])

        layout.addWidget(root)