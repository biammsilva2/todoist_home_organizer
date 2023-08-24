import os
from todoist_api_python.api import TodoistAPI


class TodoIstService:

    def __init__(self):
        token = os.getenv('TODOIST_API_TOKEN')
        if not token:
            raise ValueError('You need to set up the TODOIST token')
        self.api = TodoistAPI(token)

    def get_projects(self):
        return self.api.get_projects()

    def get_project_by_name(self, project_name):
        projects = self.get_projects()
        return next(
            (project for project in projects
             if project.name == project_name)
        )

    def get_sections_from_project(self, project):
        return self.api.get_sections(project_id=project.id)

    def get_section_by_name(self, project, section_name):
        sections = self.get_sections_from_project(project)
        return next(
            (section for section in sections
             if section.name == section_name)
        )

    def get_tasks(self, project, section):
        return self.api.get_tasks(
            project_id=project.id,
            section_id=section.id
        )

    def get_tasks_list(self, project, section):
        tasks = self.api.get_tasks(
            project_id=project.id,
            section_id=section.id
        )
        return [task.content for task in tasks]
