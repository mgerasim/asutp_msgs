import csv
import datetime

from openpyxl import load_workbook
from peewee import IntegrityError

from app.helpers.extract_nps_from_file_name_helper import ExtractNpsFromFileNameHelper
from app.message.processing.fetchers.field_fetcher import FieldFetcher
from app.message.processing.processors.data_processor import DataProcessor
from app.message.processing.processors.event_processor import EventProcessor
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

        processor = DataProcessor() #EventProcessor()

        processor.begin_prepare(file_name=file_name)

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

            processor.row_processing(columns, row)

        processor.end_prepare()
