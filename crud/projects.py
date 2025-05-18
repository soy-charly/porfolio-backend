from models import ProjectModel
from database import projects_collection
from bson import ObjectId
from datetime import datetime

async def get_all_projects():
    projects = []
    async for project in projects_collection.find():
        projects.append(ProjectModel(**project))
    return projects

async def create_project(project: ProjectModel):
    project_dict = project.dict(by_alias=True)
    project_dict["createdAt"] = datetime.utcnow()
    project_dict["updatedAt"] = datetime.utcnow()
    result = await projects_collection.insert_one(project_dict)
    return ProjectModel(**{**project_dict, "_id": result.inserted_id})
