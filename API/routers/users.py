import auth
from ioc import ioc

from routers.responses import Collection
from models.user import UserIn, UserOut, AuthUser
from fastapi import APIRouter, status, HTTPException, Depends

router = APIRouter()
REPOSITORY = ioc.get_user_repository()


@router.get('/users/me', tags=["users"])
async def get_users_me(current_user: AuthUser = Depends(auth.get_current_user)):
    return current_user


@router.get('/users', response_model=Collection, tags=["users"])
async def get_all(startDate: str = '', endDate: str = '', pageNumber:int = 1, pageSize:int = 10):
    print(startDate, endDate)

    data = REPOSITORY.read_all()
    response = {
        'pageNumber': pageNumber,
        'pageSize': len(data),
        'list': data
    }
    return response


@router.get('/users/{username}', response_model=UserOut, tags=["users"],
            responses={404: {"Message": str}})
async def get(username: str):
    system_user = REPOSITORY.read_username(username)
    if system_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return UserOut.parse_obj(REPOSITORY.read_username(username))


@router.post('/users/', response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=["users"],
             responses={409: {"Message": str}})
async def post(user: UserIn):
    system_user = REPOSITORY.read_username(user.username)
    if system_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username is already taken.')
    user.password = auth.fake_hash_password(user.password)
    dto = user.dict()
    REPOSITORY.create(dto)

    return user