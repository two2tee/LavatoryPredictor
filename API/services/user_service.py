

class UserService():

    def __init__(self, user_repository, auth_service):
        self._user_repository = user_repository
        self._auth_service = auth_service


    def create_user(self, dto):
        dto.password = self._auth_service.fake_hash_password(dto.password)
        return self._user_repository.create(dto.dict())

    def get_all_users(self, pageSize):
        return self._user_repository.read_all_users(pageSize)

    def get_user(self, username):
        return self._user_repository.read_username(username)