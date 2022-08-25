from peewee import fn

from app.core.models.base_model import db
from app.models.event import Event


class CurrentFileNameListHelper:
    @staticmethod
    def load():
        query = Event.select(Event.file_name, fn.Count(Event.file_name)).group_by(Event.file_name).tuples()
        list = []
        for row in query:
            list.append(str(row[0]))
        return list
