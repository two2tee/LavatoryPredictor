import settings
from fastapi import Depends
from models.user import UserAuth
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_ENDPOINT)


class AuthService:
    def __init__(self):
        pass

    def fake_hash_password(self, password: str):
        return 'fakehashed' + password

    def fake_decode_token(self, token):
        return UserAuth(
            username=token + ' fakedecoded'
        )

    def is_valid_user(self, user, password):
        hashed_password = self.fake_hash_password(password)
        return hashed_password == user['password']

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        user = self.fake_decode_token(token)
        return user
