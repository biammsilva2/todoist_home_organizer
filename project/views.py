from fastapi import APIRouter
from services import TodoIstService

project_router = APIRouter(prefix='/project')


@project_router.get("/")
async def read_projects():
    service = TodoIstService()
    projects = service.get_projects()
    return projects


@project_router.get("/{project_name}/section")
async def read_sections_by_project(project_name):
    service = TodoIstService()
    project = service.get_project_by_name(project_name)
    return service.get_sections_from_project(project)


@project_router.get("/{project_name}/section/{section_name}/tasks")
async def read_tasks_from_section(project_name, section_name):
    service = TodoIstService()
    project = service.get_project_by_name(project_name)
    section = service.get_section_by_name(project, section_name)
    return service.get_tasks_completed(project, section)
