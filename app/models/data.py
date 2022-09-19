import datetime

from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField
from peewee import BooleanField
from peewee import CharField
from peewee import TextField

from app.core.models.base_model import BaseModel


class Data(BaseModel):
    id = AutoField(null=False)
    date = DateTimeField(column_name='date', null=False)
    count_total = IntegerField(column_name='count_total', null=False)
    count_severity_info = IntegerField(column_name='count_severity_info', null=False)
    count_severity_warning = IntegerField(column_name='count_severity_warning', null=False)
    count_severity_critical = IntegerField(column_name='count_severity_critical', null=False)
    nps = TextField(column_name='nps', null=False)

    class Meta:
        table_name = 'Data'

        indexes = (
            (('date', 'nps'), True),
        )
