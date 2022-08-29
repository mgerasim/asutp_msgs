import datetime

from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField
from peewee import BooleanField
from peewee import CharField
from peewee import TextField

from app.core.models.base_model import BaseModel


class File(BaseModel):
    id = AutoField(null=False)
    file_name = TextField(column_name='file_name', index=True, unique=True, null=True)
    message_max_date = DateTimeField(column_name='message_max_date', null=True)
    date_started = DateTimeField(column_name='date_started', null=True)
    date_ended = DateTimeField(column_name='date_ended', null=True)
    count_added = IntegerField(column_name='count_added', null=True)
    count_duplicated = IntegerField(column_name='count_duplicated', null=True)
    error_msg = TextField(column_name='error_msg', null=True)

    class Meta:
        table_name = 'Files'
