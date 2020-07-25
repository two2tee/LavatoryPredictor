from services import auth_service

from ioc import ioc
from routers.responses import Collection
from models.user import UserBase, UserCreateRequest, UserAuth, UserCreateResponse
from fastapi import APIRouter, status, HTTPException, Depends

router = APIRouter()
REPOSITORY = ioc.get_user_repository()
USER_SERVICE = ioc.get_user_service()
AUTH_SERVICE = ioc.get_auth_service()

@router.get('/users/me', tags=["users"])
async def get_users_me(current_user: UserAuth = Depends(AUTH_SERVICE.get_current_user)):
    return current_user


@router.get('/users', response_model=Collection, tags=["users"])
async def get_all(pageSize:int = 10):

    data = USER_SERVICE.get_all_users(pageSize)
    response = {
        'pageSize': len(data),
        'list': data
    }
    return response


@router.get('/users/{username}', response_model=UserBase, tags=["users"], responses={404: {"Message": str}})
async def get(username: str):
    user = USER_SERVICE.get_user(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return UserBase.parse_obj(user)


@router.post('/users/', response_model=UserCreateResponse, status_code=status.HTTP_201_CREATED, tags=["users"], responses={409: {"Message": str}})
async def post(user: UserCreateRequest):
    existing_user = USER_SERVICE.get_user(user.username)
    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username is already taken.')
    created_user = USER_SERVICE.create_user(user)
    return UserCreateResponse.parse_obj(created_user)