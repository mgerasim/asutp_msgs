from peewee import fn

from app.models.file import File


class CurrentFileNameListHelper:
    @staticmethod
    def load():
        query = File.select(File.file_name).tuples()
        list = []
        for row in query:
            list.append(str(row[0]))
        return list
