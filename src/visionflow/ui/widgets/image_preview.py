from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
)


class ImagePreview(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Image Preview")
        title.setStyleSheet("""
        QLabel{
            font-size:16px;
            font-weight:bold;
        }
        """)

        self.importButton = QPushButton("Import Images")

        self.listWidget = QListWidget()
        self.listWidget.setIconSize(QSize(80, 80))

        layout.addWidget(title)
        layout.addWidget(self.importButton)
        layout.addWidget(self.listWidget)

        self.importButton.clicked.connect(self.importImages)

    def importImages(self):

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Images",
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )

        if not files:
            return

        self.listWidget.clear()

        for file in files:

            pixmap = QPixmap(file)

            icon = QIcon(
                pixmap.scaled(
                    80,
                    80,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

            item = QListWidgetItem(icon, file)

            self.listWidget.addItem(item)