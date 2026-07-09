from PySide6.QtWidgets import QLabel, QStatusBar


class MainStatusBar(QStatusBar):

    def __init__(self):
        super().__init__()

        self.showMessage("Ready")

        gpu = QLabel("GPU Ready")

        self.addPermanentWidget(gpu)