from PySide6.QtWidgets import QWidget,QHBoxLayout

from visionflow.ui.widgets.project_tree import ProjectTree
from visionflow.ui.widgets.image_preview import ImagePreview


class ImagePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.addWidget(ProjectTree(),1)

        layout.addWidget(ImagePreview(),3)