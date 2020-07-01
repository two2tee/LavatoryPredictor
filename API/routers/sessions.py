import uuid
from fastapi import APIRouter
from ioc import ioc

router = APIRouter()
REPOSITORY = ioc.get_session_repository()

'''TEST'''
@router.get('/sessions', tags=["sessions"])
async def get_all(startDate: str = '', endDate: str = '', pageNumber:int = 1, pageSize:int = 10):
    print(startDate, endDate)
    return REPOSITORY.read_all()


@router.get('/sessions/{session_id}', tags=["sessions"])
async def get(session_id: uuid.UUID):
    return REPOSITORY.read(str(session_id))
