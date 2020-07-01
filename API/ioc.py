import settings
from database import user_repository, session_repository


class Ioc:
    def __init__(self):
        self._user_repository = None
        self._session_repository = None

    def get_user_repository(self):
        if self._user_repository is None:
            self._user_repository = user_repository.InMemoryRepository()
        return self._user_repository

    def get_session_repository(self):
        if self._session_repository is None:
            self._session_repository = session_repository.InMemoryRepository()
        return self._session_repository


ioc = Ioc()
