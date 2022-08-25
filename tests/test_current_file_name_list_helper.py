from unittest import TestCase

from app.core.models.base_model import db, db2
from app.helpers.current_file_name_list_helper import CurrentFileNameListHelper
from app.models.event import Event


class TestCurrentFileNameHelper(TestCase):
    def test_load(self):

        db2.connect()

        Event.create_table()

        result = CurrentFileNameListHelper.load()


        for row in result:
            print(row)

        #self.assertIsNotNone(result)
