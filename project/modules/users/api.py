from fastapi import Request, status, APIRouter
from project.modules.users.models import UserCreateRequest, UserResponse
from project.modules.users.service import UserService
from project.core.base_classes.base_model import PositiveInt32


users_router = APIRouter(tags=["Users"])


@users_router.get(
    "/users/",
    summary="Get all users",
)
async def get_all_users(request: Request) -> list[UserResponse]:
    service = UserService()
    return await service.get_users()


@users_router.get(
    "/users/{user_id}/",
    summary="Get user",
)
async def get_user(request: Request, user_id: PositiveInt32) -> UserResponse:
    service = UserService()
    return await service.get_user(user_id)


@users_router.post(
    "/users/",
    summary="Create user",
    status_code=status.HTTP_201_CREATED,
)
async def create_user(request: Request, user: UserCreateRequest) -> UserResponse:
    service = UserService()
    return await service.create_user(user)
