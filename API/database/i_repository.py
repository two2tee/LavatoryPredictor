import uuid
from abc import ABCMeta, abstractmethod


class IRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, entity): raise NotImplementedError

    @abstractmethod
    def read_all(self): raise NotImplementedError

    @abstractmethod
    def read(self, entity_id): raise NotImplementedError

    @abstractmethod
    def update(self, entity_id, entity): raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id): raise NotImplementedError


class BaseRepository(IRepository):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.database = []

    def create(self, entity):
        entity['id'] = uuid.uuid4
        self.database.append(entity)
        return entity['id']

    def read_all(self):
        return self.database

    def read(self, entity_id):
        return next((entity for entity in self.database if entity['id'] == entity_id), None)

    def update(self, entity_id, entity):
        index = next((i for i, entity in enumerate(self.database) if entity['id'] == entity_id), None)
        if index:
            self.database[index] = entity
            return entity_id
        return None

    def delete(self, entity_id):
        updated_database = [entity for entity in self.database if entity['id'] != entity_id]
        is_updated = len(updated_database) != len(self.database)
        self.database = updated_database
        return is_updated