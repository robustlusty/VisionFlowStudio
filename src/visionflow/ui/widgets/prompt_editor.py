from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)


class PromptEditor(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Prompt Studio")
        title.setStyleSheet("""
            QLabel{
                font-size:18px;
                font-weight:bold;
            }
        """)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText(
            "Input master prompt here..."
        )

        layout.addWidget(title)
        layout.addWidget(self.editor)