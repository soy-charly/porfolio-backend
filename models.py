from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from bson import ObjectId
from datetime import datetime

SkillLevel = Literal["Aprendiendo", "Básico", "Medio", "Avanzado"]
Category   = Literal["Frontend", "Backend", "Other"]

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        # Pydantic v2 usará este validador
        yield cls.validate

    @classmethod
    def validate(cls, v, info=None):
        # info es el segundo parámetro que Pydantic le pasa
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        schema = handler(core_schema)
        schema.update(type="string")
        return schema

class SkillModel(BaseModel):
    id:   PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    category: Category
    level:    SkillLevel
    icon:     str
    description: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

class ProjectModel(BaseModel):
    id:   PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title:       str
    description: str
    imageUrl:    str
    technologies: List[str]
    githubUrl:   Optional[str] = None
    liveUrl:     Optional[str] = None
    createdAt:   datetime = Field(default_factory=datetime.utcnow)
    updatedAt:   datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat()
        }
