from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QSplitter, QWidget

from visionflow.ui import workspace
from visionflow.ui.widgets.navigation_panel import NavigationPanel
from visionflow.ui.statusbar import MainStatusBar
from visionflow.ui.toolbar import MainToolbar
from visionflow.ui.workspace_manager import WorkspaceManager
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

        navigation = NavigationPanel()
        navigation.setFixedWidth(240)

        splitter.addWidget(navigation)

        workspace = WorkspaceManager()

        splitter.addWidget(workspace)

        splitter.setSizes([230, 1370])