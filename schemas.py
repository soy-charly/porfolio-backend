from pydantic import BaseModel
from typing import Optional, List, Literal

SkillLevel = Literal["Aprendiendo", "Básico", "Medio", "Avanzado"]
Category = Literal["Frontend", "Backend", "Other"]

class SkillCreate(BaseModel):
    name: str
    category: Category
    level: SkillLevel
    icon: str
    description: str

class ProjectCreate(BaseModel):
    title: str
    description: str
    imageUrl: str
    technologies: List[str]
    githubUrl: Optional[str]
    liveUrl: Optional[str]
