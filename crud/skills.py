from models import SkillModel
from database import skills_collection
from bson import ObjectId

async def get_all_skills():
    skills = []
    async for skill in skills_collection.find():
        skills.append(SkillModel(**skill))
    return skills

async def create_skill(skill: SkillModel):
    skill_dict = skill.dict(by_alias=True)
    result = await skills_collection.insert_one(skill_dict)
    return SkillModel(**{**skill_dict, "_id": result.inserted_id})
