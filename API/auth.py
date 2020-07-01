
import settings
from fastapi import Depends
from models.user import AuthUser
from fastapi.security import OAuth2PasswordBearer

# Set OAuth 2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_ENDPOINT)


def fake_hash_password(password: str):
    return 'fakehashed' + password


def fake_decode_token(token):
    return AuthUser(
        username=token + ' fakedecoded'
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user