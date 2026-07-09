from PySide6.QtWidgets import QListWidget, QListWidgetItem


class Sidebar(QListWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)

        menus = [
            "🏠 Dashboard",
            "🖼 Image Manager",
            "✍ Prompt Studio",
            "🎬 Storyboard",
            "📦 Batch Queue",
            "🎞 Render",
            "📂 Outputs",
            "📜 History",
            "🔌 Plugins",
            "⚙ Settings",
        ]

        for m in menus:
            self.addItem(QListWidgetItem(m))

        self.setCurrentRow(0)