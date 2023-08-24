from fastapi import FastAPI
from dotenv import load_dotenv
from project.views import project_router

load_dotenv()

app = FastAPI()

app.include_router(project_router)

@app.get("/")
async def root():
    return {"message": "Home organizer app"}
