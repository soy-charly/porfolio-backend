from fastapi import FastAPI
from crud.skills import get_all_skills, create_skill
from crud.projects import get_all_projects, create_project
from models import SkillModel, ProjectModel

app = FastAPI()

@app.get("/skills")
async def read_skills():
    return await get_all_skills()

@app.post("/skills")
async def add_skill(skill: SkillModel):
    return await create_skill(skill)

@app.get("/projects")
async def read_projects():
    return await get_all_projects()

@app.post("/projects")
async def add_project(project: ProjectModel):
    return await create_project(project)
