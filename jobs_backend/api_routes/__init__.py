from fastapi import APIRouter

from api_routes.version_1 import route_jobs

api_router = APIRouter()
api_router.include_router(router=route_jobs.router, prefix='/jobs', tags=['jobs'])
