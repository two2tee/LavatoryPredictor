from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Color(str, Enum):
    black = 'black',
    green = 'green',
    white = 'beige',
    yellow = 'yellow',
    brown = 'brown',
    darkbrown = 'darkbrown',
    orange = 'orage',
    red = 'red'


class Session(BaseModel):
    color: Color