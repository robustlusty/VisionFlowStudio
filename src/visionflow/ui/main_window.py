from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QSplitter, QWidget

from visionflow.ui.sidebar import Sidebar
from visionflow.ui.statusbar import MainStatusBar
from visionflow.ui.toolbar import MainToolbar
from visionflow.ui.workspace import Workspace
from visionflow.ui.theme import load_stylesheet

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VisionFlow Studio")

        self.resize(1600, 950)

        self.setMinimumSize(1280, 800)

        self.setStyleSheet(load_stylesheet())
        
        self.addToolBar(MainToolbar())

        self.setStatusBar(MainStatusBar())

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Horizontal)

        layout.addWidget(splitter)

        splitter.addWidget(Sidebar())

        splitter.addWidget(Workspace())

        splitter.setSizes([230, 1370])