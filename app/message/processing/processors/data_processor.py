from abc import ABC

from app.message.processing.fetchers.field_fetcher import FieldFetcher
from app.message.processing.processors.base.base_processor import BaseProcessor
import pandas as pd

from app.models.data import Data


class DataProcessor(BaseProcessor, ABC):
    datetime_column = []
    severity_column = []

    def row_processing(self, columns, row):

        datetime_field = FieldFetcher.DateCreatedFetch(columns, row)

        severity_field = FieldFetcher.SeverityFetch(columns, row)

        self.datetime_column.append(datetime_field)

        self.severity_column.append(severity_field)

        if datetime_field > self.file.message_max_date:
            self.file.message_max_date = datetime_field

    def begin_prepare(self, file_name):
        self.datetime_column = []
        self.severity_column = []
        super().begin_prepare(file_name)

    def end_prepare(self):
        data = {'EventTime': self.datetime_column, 'Severity': self.severity_column}
        df = pd.DataFrame(data)

        s = pd.to_datetime(df['EventTime'])
        df_count_total = s.groupby(s.dt.floor('d')).size().reset_index(name='count_total')

        s = pd.to_datetime((df[df.Severity == 0]['EventTime']))
        df_count_severity_info = s.groupby(s.dt.floor('d')).size().reset_index(name='count_severity_info')

        s = pd.to_datetime((df[df.Severity == 1]['EventTime']))
        df_count_severity_warning = s.groupby(s.dt.floor('d')).size().reset_index(name='count_severity_warning')

        s = pd.to_datetime((df[df.Severity == 2]['EventTime']))
        df_count_severity_critical = s.groupby(s.dt.floor('d')).size().reset_index(name='count_severity_critical')

        df = pd.merge(left=df_count_total, right=df_count_severity_info, how='left', on='EventTime')
        df = pd.merge(left=df, right=df_count_severity_warning, how='left', on='EventTime')
        df = pd.merge(left=df, right=df_count_severity_critical, how='left', on='EventTime')

        df.fillna(0)

        for index, row in df.iterrows():
            print(row['EventTime'].date())
            data = Data.get_or_none(Data.date == row['EventTime'].date(), Data.nps == self.nps)
            if data is None:
                data = Data()
                data.date = row['EventTime'].date()
                data.count_total = 0
                data.count_severity_info = 0
                data.count_severity_warning = 0
                data.count_severity_critical = 0
                data.nps = self.nps
            data.count_total += row['count_total']
            data.count_severity_info += row['count_severity_info']
            data.count_severity_warning += row['count_severity_warning']
            data.count_severity_critical += row['count_severity_critical']
            data.date = row['EventTime'].date()
            data.save()

        super().end_prepare()
