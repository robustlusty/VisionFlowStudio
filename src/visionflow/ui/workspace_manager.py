from PySide6.QtWidgets import QStackedWidget

from visionflow.ui.pages.video_page import VideoPage
from visionflow.ui.pages.image_page import ImagePage
from visionflow.ui.pages.prompt_page import PromptPage
from visionflow.ui.pages.plugin_page import PluginPage
from visionflow.ui.pages.workflow_page import WorkflowPage
from visionflow.ui.pages.database_page import DatabasePage
from visionflow.ui.pages.settings_page import SettingsPage


class WorkspaceManager(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.video = VideoPage()
        self.image = ImagePage()
        self.prompt = PromptPage()
        self.plugin = PluginPage()
        self.workflow = WorkflowPage()
        self.database = DatabasePage()
        self.settings = SettingsPage()

        self.addWidget(self.video)
        self.addWidget(self.image)
        self.addWidget(self.prompt)
        self.addWidget(self.plugin)
        self.addWidget(self.workflow)
        self.addWidget(self.database)
        self.addWidget(self.settings)

        self.setCurrentWidget(self.prompt)