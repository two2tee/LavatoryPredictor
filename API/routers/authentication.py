from services import auth_service
from ioc import ioc
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends

from models.user import UserAuth

router = APIRouter()
USER_SERVICE = ioc.get_user_service()
AUTH_SERVICE = ioc.get_auth_service()


@router.post('/token', tags=['authentication'])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USER_SERVICE.get_user(form_data.username)
    if not user or not AUTH_SERVICE.is_valid_user(user, form_data.password):
        raise HTTPException(status_code=401, detail='Incorrect username or password')

    user = UserAuth(**user)
    return {"access_token": user.username, "token_type": "bearer"}