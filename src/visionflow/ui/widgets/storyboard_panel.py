from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
)


class StoryboardPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Storyboard")
        title.setStyleSheet("""
            QLabel{
                font-size:16px;
                font-weight:bold;
            }
        """)

        preview = QFrame()
        preview.setFrameShape(QFrame.StyledPanel)

        preview_layout = QVBoxLayout(preview)

        preview_layout.addStretch()

        preview_layout.addWidget(
            QLabel("Storyboard Preview")
        )

        preview_layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(preview)