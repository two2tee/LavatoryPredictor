import uuid
from database.i_repository import IRepository


class InMemoryRepository(IRepository):
    def __init__(self):
        self.data = [{'id':'f40a1276-68a7-4d15-8e30-26b2eadf348a'},{'id':'f40a1276-68a7-4d15-8e30-26b2eadf348b'}]

    def create(self, entity):
        entity['id'] = uuid.uuid4
        self.data.append(entity)
        return entity['id']

    def read_all(self):
        return self.data

    def read(self, entity_id):
        return next((entity for entity in self.data if entity['id'] == entity_id), None)

    def update(self, entity_id, entity):
        index = next((i for i, entity in enumerate(self.data) if entity['id'] == entity_id), None)
        if index:
            self.data[index] = entity
            return entity_id
        return None

    def delete(self, entity_id):
        data = [entity for entity in self.data if entity['id'] != entity_id]
        is_updated = len(data) != len(self.data)
        self.data = data
        return is_updated
