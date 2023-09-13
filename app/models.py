import uuid
from typing import Optional, List
from pydantic import BaseModel, Field


class ProjectVideos(BaseModel):
    video_1: Optional[dict]
    video_2: Optional[dict]
    video_3: Optional[dict]

    class Config:
        json_schema_extra = {
            "example": {
                "video_1": {
                    "video_title": "Google",
                    "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                },
                "video_2": {
                    "video_title": "Google",
                    "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                },
                "video_3": {
                    "video_title": "Google",
                    "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                },
            }
        }


class ProjectDescription(BaseModel):
    paragraph_1: str
    paragraph_2: str

    class Config:
        json_schema_extra = {
            "example": {
                "paragraph_1": "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University.",
                "paragraph_2": "Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock.",
            }
        }


class Job(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    company_name: str = Field(...)
    skills: List[str] = Field(...)
    company_url: str = Field(...)
    company_description: str = Field(...)
    project_description: dict = Field(...)
    project_videos: dict = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Senior Software Engineer",
                "company_name": "Google",
                "skills": ["Python", "Django", "Flask", "FastAPI"],
                "company_description": "Google is an American multinational technology.",
                "project_description": {
                    "paragraph_1": "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University.",
                    "paragraph_2": "Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock.",
                },
                "project_videos": {
                    "video_1": {
                        "video_title": "Google",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                    "video_2": {
                        "video_title": "Google",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                    "video_3": {
                        "video_title": "Google",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                },
                "company_url": "https://www.google.com/",
            }
        }


class JobUpdate(BaseModel):
    title: Optional[str]
    company_name: Optional[str]
    skills: Optional[List[str]]
    company_url: Optional[str]
    company_description: Optional[str]
    project_description: Optional[ProjectDescription]
    project_videos: Optional[ProjectVideos]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Data Science Engineer",
                "company_name": "Enron",
                "skills": ["Python", "Django", "Flask", "FastAPI"],
                "company_description": "Enron Corporation was an American energy, commodities, and services company based in Houston, Texas.",
                "project_description": {
                    "paragraph_1": "Enron was founded in Omaha, Nebraska, in 1985 as the Northern Natural Gas Company.",
                    "paragraph_2": "It was reorganized in 1979 as the main subsidiary of a holding company, InterNorth, which was a diversified energy and energy-related products company.",
                },
                "project_videos": {
                    "video_1": {
                        "video_title": "Enron",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                    "video_2": {
                        "video_title": "Enron",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                    "video_3": {
                        "video_title": "Enron",
                        "video_url": "https://www.youtube.com/watch?v=JN3o2sLniKM",
                    },
                },
                "company_url": "https://www.enron.com/",
            }
        }
