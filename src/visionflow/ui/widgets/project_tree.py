from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem,
)


class ProjectTree(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Project Explorer")

        title.setStyleSheet("""
        QLabel{
            font-size:16px;
            font-weight:bold;
        }
        """)

        self.tree = QTreeWidget()

        self.tree.setHeaderHidden(True)

        layout.addWidget(title)

        layout.addWidget(self.tree)

        self.buildDemo()

    def buildDemo(self):

        project = QTreeWidgetItem(["📂 Demo Project"])

        product = QTreeWidgetItem(["📦 Product 001"])

        images = QTreeWidgetItem(["🖼 Images"])

        prompts = QTreeWidgetItem(["✍ Prompts"])

        videos = QTreeWidgetItem(["🎬 Videos"])

        images.addChild(
            QTreeWidgetItem(["image01.jpg"])
        )

        images.addChild(
            QTreeWidgetItem(["image02.jpg"])
        )

        prompts.addChild(
            QTreeWidgetItem(["Prompt 01"])
        )

        prompts.addChild(
            QTreeWidgetItem(["Prompt 02"])
        )

        product.addChild(images)

        product.addChild(prompts)

        product.addChild(videos)

        project.addChild(product)

        self.tree.addTopLevelItem(project)

        self.tree.expandAll()