from fastapi import APIRouter, Body, Depends, Form, HTTPException, status
from app.admin import authenticate

# Request, Response, HTTPException,
from app.database import database
from app.models import (
    CreateJobRequest,
    Job,
    JobUpdate,
    ProjectDescription,
    ProjectVideos,
)
from fastapi.encoders import jsonable_encoder

router = APIRouter()

collection = database["experience"]

jobs_db = []


@router.get("/", response_description="List all jobs")
async def list_jobs():
    jobs = list(collection.find({}, limit=100))
    formatted_jobs = [
        {
            "_id": str(job["_id"]),
            "title": job["title"],
            "company_name": job["company_name"],
            "company_url": job["company_url"],
            "company_description": job["company_description"],
            "project_description": job["project_description"],
            "project_videos": job["project_videos"],
            "skills": job["skills"],
        }
        for job in jobs
    ]
    return formatted_jobs


@router.post("/jobs/", response_model=Job, response_description="Create a new job")
async def create_job(
    title: str = Form(...),
    company_name: str = Form(...),
    company_url: str = Form(...),
    company_description: str = Form(...),
    project_description: ProjectDescription = Form(...),
    project_videos: ProjectVideos = Form(...),
    skills: list[str] = Form(...),
    authenticated: bool = Depends(authenticate),
):
    if not authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")

    job_data = {
        "title": title,
        "company_name": company_name,
        "company_url": company_url,
        "company_description": company_description,
        "project_description": project_description.model_dump(),
        "project_videos": project_videos.model_dump(),
        "skills": skills,
    }
    new_job = collection.insert_one(job_data)
    created_job = collection.find_one({"_id": new_job.inserted_id})
    return created_job
