from fastapi import APIRouter, Body, status
# Request, Response, HTTPException,
from db import database
from models import Job
from fastapi.encoders import jsonable_encoder

router = APIRouter()

collection = database['experience']


@router.get("/", response_description="List all jobs")
async def list_jobs():
    jobs = list(collection.find({}, limit=100))
    formatted_jobs = [{"title": job["title"],
                       "company_name": job["company_name"],
                       "skills": job["skills"]} for job in jobs]

    return formatted_jobs


@router.post("/", response_description="Create a new job",
             status_code=status.HTTP_201_CREATED, response_model=Job)
def create_job(job: Job = Body(...)):
    job = jsonable_encoder(job)
    new_job = collection.insert_one(job)
    created_job = collection.find_one(
        {"_id": new_job.inserted_id}
    )

    return created_job
