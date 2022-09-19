from abc import ABC

from app.helpers.extract_nps_from_file_name_helper import ExtractNpsFromFileNameHelper
from app.message.processing.fetchers.field_fetcher import FieldFetcher
from app.message.processing.processors.base.base_processor import BaseProcessor
from app.models.event import Event


class EventProcessor(BaseProcessor, ABC):
    def row_processing(self, columns, row):
        event = Event()
        event.date_created = FieldFetcher.DateCreatedFetch(columns, row)
        event.object = FieldFetcher.ObjectFetch(columns, row)
        event.severity = FieldFetcher.SeverityFetch(columns, row)
        event.message = FieldFetcher.MessageFetch(columns, row)
        event.file_name = self.file.file_name
        event.nps = self.nps

        if event.date_created > self.file.message_max_date:
            self.file.message_max_date = event.date_created

        try:
            event.save()
            self.file.count_added += 1
        except Exception as e:
            if 'UNIQUE constraint failed' in str(e):
                self.file.count_duplicated += 1
            if 'Duplicate entry' in str(e):
                self.file.count_duplicated += 1
            print(str(e))
            self.file.error_msg = str(e)