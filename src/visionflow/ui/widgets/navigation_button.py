from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.setCheckable(True)

        self.setMinimumHeight(42)
        self.setStyleSheet("""
            QPushButton{
                text-align:left;
                padding-left:16px;
                border:none;
                border-radius:6px;
                background:transparent;
            }

            QPushButton:hover{
                background:#313244;
            }

            QPushButton:checked{
                background:#3B82F6;
                color:white;
                font-weight:bold;
            }
        """)