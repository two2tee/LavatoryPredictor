from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    name: str
    birthdate: Optional[datetime] = None
    sex: Optional[datetime] = None
    height: Optional[int] = None
    weight: Optional[int] = None


class UserOut(BaseModel):
    username: str
    name: str
    birthdate: Optional[datetime] = None
    sex: Optional[datetime] = None
    height: Optional[int] = None
    weight: Optional[int] = None

class AuthUser(BaseModel):
    username: str
