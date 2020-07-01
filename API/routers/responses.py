from pydantic import BaseModel

class Collection(BaseModel):
    pageSize: int
    pageNumber: int
    list: list