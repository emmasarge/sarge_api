# sarge_api
python, mongodb, flask, fast api



## python v3

Check version:

    python3 --version

Create environment:

    python3 -m venv venv

Activate environment:

    On Windows:
        venv\Scripts\activate

    On macOS and Linux:
        source venv/bin/activate



    pip install fastapi uvicorn


### to start this app
    python3 -m venv venv

    source venv/bin/activate

    python -m pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv uvicorn

    mkdir app

    cd app
    touch main.py routes.py models.py .env

### to run

        python3 -m uvicorn main:app --reload


### to view in browser locally:

        http://localhost:8000/docs



### when adding dependencies:

        pip freeze > requirements.txt


### push to heroku:

        git push heroku main