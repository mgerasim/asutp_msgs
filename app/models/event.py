import datetime

from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField
from peewee import BooleanField
from peewee import CharField
from peewee import TextField

from app.core.models.base_model import BaseModel


class Event(BaseModel):
    id = AutoField(null=False)
    date_created = DateTimeField(column_name='date_created', null=False)
    source = TextField(column_name='source', null=False)
    username = TextField(column_name='username', null=False)
    priority = TextField(column_name='priority', null=False)
    message = TextField(column_name='message', null=False)
    nps = TextField(column_name='nps', null=False)
    file_name = TextField(column_name='file_name', null=False)

    class Meta:
        table_name = 'Events'

        indexes = (
            (('date_created', 'source', 'priority', 'message', 'nps'), True),
        )
