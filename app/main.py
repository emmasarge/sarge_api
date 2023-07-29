import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from db import mongodb_client, database
from routes import router
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

origins = [
    # List your frontend URLs that need access to the API
    "http://localhost",
    "http://localhost:3000",  # For development
    "https://sarge-api-55c088dc973a.herokuapp.com/",
    "https://sarge-api-2-2c274f48e1a5.herokuapp.com/",
    "https://sarge-api-23-8cdf3807bdf0.herokuapp.com/",
    "https://git.heroku.com/sarge-api-23.git"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_client():
    # Use the MongoDB connection from db.py
    app.mongodb_client = mongodb_client
    app.database = database


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(router, tags=["job"], prefix="/jobs")

if __name__ == "__main__":
    # Use os.environ.get('PORT') to get the assigned port from Heroku
    port = int(os.environ.get('PORT', 8000))
    # Run the app using uvicorn with host set to
    # '0.0.0.0' to
    # allow external connections
    uvicorn.run("main:app", host='0.0.0.0',
                port=port)
