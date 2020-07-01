import auth
from ioc import ioc
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, HTTPException, Depends

from models.user import AuthUser

router = APIRouter()
USER_REPOSITORY = ioc.get_user_repository()


@router.post('/token', tags=['authentication'])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = USER_REPOSITORY.read_username(form_data.username)
    if not db_user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    hashed_password = auth.fake_hash_password(form_data.password)
    if not hashed_password == db_user['password']:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    user = AuthUser(**db_user)
    return {"access_token": user.username, "token_type": "bearer"}