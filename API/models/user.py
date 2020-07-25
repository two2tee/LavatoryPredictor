from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    name: str
    birthdate: Optional[datetime] = None
    sex: Optional[datetime] = None
    height: Optional[int] = None
    weight: Optional[int] = None

class UserCreateRequest(UserBase):
    password: str


class UserCreateResponse(UserBase):
    createdon: datetime

class UserAuth(BaseModel):
    username: str
