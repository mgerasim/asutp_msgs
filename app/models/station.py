import datetime

from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField
from peewee import BooleanField
from peewee import CharField
from peewee import TextField

from app.core.models.base_model import BaseModel

class Station(BaseModel):
    id = AutoField(null=False)
    title = TextField(column_name='title', null=False, unique=True)
    state = IntegerField(column_name='state', null=True)
    updated_at = DateTimeField(column_name='updated_at', null=True)

    class Meta:
        table_name = 'Station'
