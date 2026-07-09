from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem,
)


class BatchQueue(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Batch Queue")
        title.setStyleSheet("""
            QLabel{
                font-size:16px;
                font-weight:bold;
            }
        """)

        self.tree = QTreeWidget()

        self.tree.setHeaderLabels([
            "Task",
            "Status"
        ])

        self.tree.setColumnWidth(0, 220)

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                "No Task",
                "Idle"
            ])
        )

        layout.addWidget(title)
        layout.addWidget(self.tree)