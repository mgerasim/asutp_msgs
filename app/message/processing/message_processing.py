
from openpyxl import load_workbook
from peewee import IntegrityError

from app.helpers.extract_nps_from_file_name_helper import ExtractNpsFromFileNameHelper
from app.models.event import Event


class MessageProcessing:
    @staticmethod
    def run(file_name):
        wb = load_workbook(file_name)
        sheet = wb.active

        index = 0
        for row in sheet.rows:
            index += 1
            if index == 1:
                continue
            event = Event()
            event.date_created = row[0].value
            event.source = row[2].value
            event.username = row[3].value
            event.priority = row[4].value
            event.message = row[5].value
            event.file_name = file_name
            event.nps = ExtractNpsFromFileNameHelper.run(file_name=file_name)

            if row[0].value is None:
                continue

            print(f"""{row[0].value} {row[2].value} {row[3].value} {row[4].value} {row[5].value} {file_name}""")

            try:
                event.save()
            except IntegrityError:
                pass





