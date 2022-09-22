from abc import ABC, abstractmethod
import datetime

from app.helpers.extract_nps_from_file_name_helper import ExtractNpsFromFileNameHelper
from app.helpers.save_nps_helper import SaveNpsHelper
from app.models.file import File


class BaseProcessor(ABC):
    file: File = None
    nps = None

    def begin_prepare(self, file_name):
        self.file = File()
        self.file.file_name = file_name
        self.file.date_started = datetime.datetime.now()
        self.file.count_added = 0
        self.file.count_duplicated = 0
        self.file.message_max_date = datetime.datetime.min

        self.nps = ExtractNpsFromFileNameHelper.run(file_name=self.file.file_name)
        SaveNpsHelper.save(self.nps)

    def end_prepare(self):
        self.file.date_ended = datetime.datetime.now()
        self.file.save()

    @abstractmethod
    def row_processing(self, columns, row):
        pass

