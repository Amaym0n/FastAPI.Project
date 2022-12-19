from fastapi import APIRouter

from api_routes.version_1 import route_users

api_router = APIRouter()

api_router.include_router(router=route_users.router, prefix='/users', tags=['users'])
