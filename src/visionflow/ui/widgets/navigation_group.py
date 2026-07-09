from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout

from visionflow.ui.widgets.navigation_button import NavigationButton


class NavigationGroup(QWidget):

    def __init__(self, title, items):
        super().__init__()

        layout = QVBoxLayout(self)

        titleLabel = QLabel(title)
        layout.addWidget(titleLabel)

        for item in items:
            layout.addWidget(NavigationButton(item))

        layout.addStretch()