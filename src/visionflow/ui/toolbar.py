from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):

    def __init__(self):
        super().__init__("Toolbar")

        self.setMovable(False)

        self.addAction("New")
        self.addAction("Open")
        self.addAction("Save")

        self.addSeparator()

        self.addAction("Run")
        self.addAction("Stop")

        self.addSeparator()

        self.addAction("Settings")