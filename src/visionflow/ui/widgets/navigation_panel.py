from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

from visionflow.ui.widgets.navigation_group import NavigationGroup


class NavigationPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(
            NavigationGroup(
                "Workspace",
                [
                    "Video",
                    "Images",
                    "Prompt",
                ]
            )
        )

        layout.addWidget(
            NavigationGroup(
                "Project",
                [
                    "Plugins",
                    "Workflow",
                    "Database",
                    "Settings",
                ]
            )
        )

        layout.addStretch()