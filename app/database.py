import os
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv

load_dotenv()

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
env_path = os.path.join(root_folder, ".env")

config = dotenv_values(env_path)
ATLAS_URI = os.environ.get("ATLAS_URI")
DB_NAME = os.environ.get("DB_NAME")

mongodb_client = MongoClient(ATLAS_URI)
database = mongodb_client[DB_NAME]
