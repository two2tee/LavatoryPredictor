import uuid
from database.i_repository import BaseRepository


class InMemoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def read_username(self, username):
        return next((user for user in self.database if user['username'] == username), None)

