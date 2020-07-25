import settings
from database import user_repository, session_repository
from services import auth_service, user_service, session_service

class Ioc:
    def __init__(self):
        self._user_repository = None
        self._session_repository = None
        self._auth_service = None
        self._user_service = None
        self._session_service = None

    def get_user_repository(self):
        if self._user_repository is None:
            self._user_repository = user_repository.InMemoryRepository()
        return self._user_repository

    def get_session_repository(self):
        if self._session_repository is None:
            self._session_repository = session_repository.InMemoryRepository()
        return self._session_repository

    def get_auth_service(self):
        if self._auth_service is None:
            self._auth_service = auth_service.AuthService()
        return self._auth_service

    def get_user_service(self):
        if self._user_service is None:
            self._user_service = user_service.UserService(self.get_user_repository(), self.get_auth_service())
        return self._user_service

    def _session_service(self):
        if self._session_service is None:
            self._session_service = session_service.SessionService(self.get_session_repository())
        return self._session_service

ioc = Ioc()
