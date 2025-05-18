from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)

# 🔥 Usamos una sola base de datos para todo
db = client["portfolio_db"]

# Cada colección es un atributo
skills_collection = db["skills"]
projects_collection = db["projects"]
