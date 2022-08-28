import csv
import datetime

from openpyxl import load_workbook
from peewee import IntegrityError

from app.helpers.extract_nps_from_file_name_helper import ExtractNpsFromFileNameHelper
from app.message.processing.fetchers.field_fetcher import FieldFetcher
from app.models.event import Event
from app.models.file import File


class MessageProcessing:
    @staticmethod
    def read_rows(file_name):
        print(f"""read_rows {file_name}""")
        import pathlib
        file_extension = pathlib.Path(file_name).suffix
        match file_extension:
            case '.xlsx':
                return MessageProcessing.read_from_xlsx(file_name)
            case '.csv':
                return MessageProcessing.read_from_csv(file_name)
            case _:
                raise Exception(f"""Неподдерживаемое расширение файла #{file_name}""")

    @staticmethod
    def read_from_xlsx(file_name):
        wb = load_workbook(file_name)
        sheet = wb.active
        return sheet.rows

    @staticmethod
    def read_from_csv(file_name):
        rows = []
        with open(file_name, "r") as f:
            data = csv.reader(f)
            for row in data:
                rows.push(row)

    @staticmethod
    def run(file_name):
        rows = MessageProcessing.read_rows(file_name)

        file = File()
        file.file_name = file_name
        file.date_started = datetime.datetime.now()
        file.count_added = 0
        file.count_duplicated = 0
        file.message_max_date = datetime.datetime.min

        index = 0
        columns = None
        for row in rows:
            index += 1
            if row[0].value is None:
                continue
            if columns is None:
                columns = row
                continue

            if row[0].value is None:
                continue

            event = Event()
            event.date_created = FieldFetcher.DateCreatedFetch(columns, row)
            event.object = FieldFetcher.ObjectFetch(columns, row)
            event.severity = FieldFetcher.SeverityFetch(columns, row)
            event.message = FieldFetcher.MessageFetch(columns, row)
            event.file_name = file_name
            event.nps = ExtractNpsFromFileNameHelper.run(file_name=file_name)

            if event.date_created > file.message_max_date:
                file.message_max_date = event.date_created

            try:
                event.save()
                file.count_added += 1
            except Exception as e:
                if 'UNIQUE constraint failed' in str(e):
                    file.count_duplicated += 1
                    continue
                if 'Duplicate entry' in str(e):
                    file.count_duplicated += 1
                    continue
                print(str(e))
                file.error_msg = str(e)

            file.date_ended = datetime.datetime.now()
            file.save()





