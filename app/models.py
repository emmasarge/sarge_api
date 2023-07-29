import uuid
from typing import Optional, List
from pydantic import BaseModel, Field


class Job(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    company_name: str = Field(...)
    skills: List[str] = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Senior Software Engineer",
                "company_name": "Google",
                "skills": ["Python", "Django", "Flask", "FastAPI"]
            }
        }


class JobUpdate(BaseModel):
    title: Optional[str]
    company_name: Optional[str]
    skills: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Data Science Engineer",
                "company_name": "Enron",
                "skills": ["Python", "Django", "Flask", "FastAPI"]
            }
        }
