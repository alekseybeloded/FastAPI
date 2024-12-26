from fastapi import FastAPI

from teams.views import router as teams_router

app = FastAPI()
app.include_router(teams_router)
