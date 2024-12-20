from fastapi import APIRouter
from scenarios.tasks import tasks_router

chaos_router = APIRouter(prefix="/chaos")
chaos_router.include_router(tasks_router)
