from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from visionflow.ui.widgets.navigation_button import NavigationButton


class NavigationGroup(QWidget):

    def __init__(self, title, items):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel(title))

        self.buttons = []

        for text, page in items:

            button = NavigationButton(text, page)

            self.buttons.append(button)

            layout.addWidget(button)

        layout.addStretch()