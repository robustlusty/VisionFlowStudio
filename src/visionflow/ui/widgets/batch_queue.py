from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem
)


class BatchQueue(QWidget):

    def __init__(self):
        super().__init__()

        layout=QVBoxLayout(self)

        title=QLabel("Batch Queue")

        title.setObjectName("PanelTitle")

        self.tree=QTreeWidget()

        self.tree.setHeaderLabels(
            ["Job","Status"]
        )

        self.tree.addTopLevelItem(
            QTreeWidgetItem(
                ["Waiting...","Idle"]
            )
        )

        layout.addWidget(title)

        layout.addWidget(self.tree)