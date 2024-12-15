from fastapi import FastAPI
from router import chaos_router

app = FastAPI()

app.include_router(chaos_router)
