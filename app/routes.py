from fastapi import APIRouter, Body, Depends, HTTPException, status
from app.admin import authenticate

# Request, Response, HTTPException,
from app.database import database
from app.models import Job, ProjectDescription, ProjectVideos
from fastapi.encoders import jsonable_encoder

router = APIRouter()

collection = database["experience"]


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


@router.post(
    "/",
    response_description="Create a new job",
    status_code=status.HTTP_201_CREATED,
    response_model=Job,
)
def create_job(
    title: str,
    company_name: str,
    company_url: str,
    company_description: str,
    project_description: ProjectDescription, 
    project_videos: ProjectVideos,
    skills: list[str],
    authenticated: bool = Depends(authenticate),
):
    if not authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    job_data = {
        "title": title,
        "company_name": company_name,
        "company_url": company_url,
        "company_description": company_description,
        "project_description": {
            "paragraph_1": project_description.paragraph_1,
            "paragraph_2": project_description.paragraph_2,
        },
        "project_videos": {
            "video_1": {
                "video_title": project_videos.video_1.video_title,
                "video_url": project_videos.video_1.video_url,
            },
        },
        "video_2": {
            "video_title": project_videos.video_2.video_title,
            "video_url": project_videos.video_2.video_url,
        },
        "video_3": {
            "video_title": project_videos.video_3.video_title,
            "video_url": project_videos.video_3.video_url,
        },
        "skills": skills,
    }

    new_job = collection.insert_one(job_data)
    created_job = collection.find_one({"_id": new_job.inserted_id})

    return created_job
