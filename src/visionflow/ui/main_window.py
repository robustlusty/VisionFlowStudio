from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QSplitter,
    QWidget,
)

from visionflow.ui.statusbar import MainStatusBar
from visionflow.ui.toolbar import MainToolBar
from visionflow.ui.theme import load_stylesheet

from visionflow.ui.widgets.navigation_panel import NavigationPanel
from visionflow.ui.workspace_manager import WorkspaceManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VisionFlow Studio")

        self.resize(1600, 950)

        self.setMinimumSize(1280, 800)

        self.setStyleSheet(load_stylesheet())

        self.addToolBar(MainToolBar())

        self.setStatusBar(MainStatusBar())

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Horizontal)

        layout.addWidget(splitter)

        # =========================
        # Left Navigation
        # =========================

        navigation = NavigationPanel()

        navigation.setFixedWidth(240)

        # =========================
        # Workspace
        # =========================

        workspace = WorkspaceManager()

        navigation.connectWorkspace(workspace)

        # =========================
        # Splitter
        # =========================

        splitter.addWidget(navigation)

        splitter.addWidget(workspace)

        splitter.setSizes([240, 1360])