from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QVBoxLayout,QSplitter

from visionflow.ui.widgets.prompt_editor import PromptEditor
from visionflow.ui.widgets.storyboard_panel import StoryboardPanel
from visionflow.ui.widgets.image_preview import ImagePreview
from visionflow.ui.widgets.batch_queue import BatchQueue


class Workspace(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout(self)

        layout.setContentsMargins(6,6,6,6)

        root=QSplitter(Qt.Horizontal)

        layout.addWidget(root)

        left=QSplitter(Qt.Vertical)

        right=QSplitter(Qt.Vertical)

        left.addWidget(PromptEditor())

        left.addWidget(ImagePreview())

        right.addWidget(StoryboardPanel())

        right.addWidget(BatchQueue())

        root.addWidget(left)

        root.addWidget(right)

        root.setSizes([900,500])