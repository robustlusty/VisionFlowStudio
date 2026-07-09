from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

from visionflow.ui.widgets.navigation_group import NavigationGroup


class NavigationPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        workspaceGroup = NavigationGroup(
            "Workspace",
            [
                ("Video", "video"),
                ("Images", "image"),
                ("Prompt", "prompt"),
            ]
        )

        projectGroup = NavigationGroup(
            "Project",
            [
                ("Plugins", "plugin"),
                ("Workflow", "workflow"),
                ("Database", "database"),
                ("Settings", "settings"),
            ]
        )

        self.groups = [
            workspaceGroup,
            projectGroup
        ]

        layout.addWidget(workspaceGroup)
        layout.addWidget(projectGroup)
        layout.addStretch()

    def connectWorkspace(self, workspace):

        for group in self.groups:

            for button in group.buttons:

                button.clickedPage.connect(workspace.showPage)