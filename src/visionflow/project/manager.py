from visionflow.project.project import Project


class ProjectManager:

    def __init__(self):

        self.project = Project()

    def current(self):

        return self.project

    def new(self):

        self.project = Project()

        return self.project