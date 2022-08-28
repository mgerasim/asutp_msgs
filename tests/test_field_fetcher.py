import datetime
from unittest import TestCase

from app.message.processing.fetchers.field_fetcher import FieldFetcher


class Column:
    def __init__(self, value):
        self.value = value


class TestFieldFetcher(TestCase):
    def test_date_created_fetch(self):

        columns = [Column('Дата')]
        row = [Column('2022-05-31 23:58:23.002')]
        value = FieldFetcher.DateCreatedFetch(columns=columns,
                                              row=row)
        #self.assertEqual(first=row[0].value, second=value)

        self.assertEqual(type(value), datetime.datetime)


    def test_message_fetch(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('Текст')]
        value = FieldFetcher.MessageFetch(columns=columns,
                                          row=row)
        self.assertEqual(first=row[1].value,
                         second=value)


    def test_message_fetch_1(self):
        columns = [Column('Дата'), Column('Текст сообщения')]
        row = [Column('11.11.1111'), Column('Текст')]
        value = FieldFetcher.MessageFetch(columns=columns,
                                          row=row)
        self.assertEqual(first=row[1].value,
                         second=value)


    def test_object_fetch_1(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('Объект.Текст')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='Объект',
                         second=value)


    def test_object_fetch_2(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('Объект_Текст')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='Объект',
                         second=value)


    def test_object_fetch_3(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('.Объект.Текст')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='Объект',
                         second=value)


    def test_object_fetch_4(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('.Объект_Текст')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='Объект',
                         second=value)


    def test_object_fetch_5(self):
        columns = [Column('Дата'), Column('Сообщение'), Column('Объект')]
        row = [Column('11.11.1111'), Column('.Объект_Текст'), Column('TEST')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='TEST',
                         second=value)


    def test_object_fetch_6(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('ХОЗ.-ПИТЬЕВОЙ НАСОС НВ1. ОТКЛЮЧЕН')]
        value = FieldFetcher.ObjectFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='ХОЗ-ПИТЬЕВОЙ НАСОС НВ1',
                         second=value)


    def test_quality_fetch(self):
        columns = [Column('Дата'), Column('Сообщение'), Column('Качество')]
        row = [Column('11.11.1111'), Column('.Объект_Текст'), Column('1')]
        value = FieldFetcher.QualityFetch(columns=columns,
                                         row=row)
        self.assertEqual(first=1,
                         second=value)


    def test_quality_fetch_1(self):
        columns = [Column('Дата'), Column('Сообщение')]
        row = [Column('11.11.1111'), Column('.Объект_Текст'), Column('1')]
        value = FieldFetcher.QualityFetch(columns=columns,
                                         row=row)
        self.assertEqual(first=None,
                         second=value)


    def test_priority_fetch(self):
        columns = [Column('Дата'), Column('Сообщение'), Column('Качество'), Column('Приоритет')]
        row = [Column('11.11.1111'), Column('.Объект_Текст'), Column('1'), Column('Нормальный')]
        value = FieldFetcher.PriorityFetch(columns=columns,
                                         row=row)
        self.assertEqual(first='Нормальный',
                         second=value)

    def test_convert_quality_to_severity(self):
        quality = 0
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(0, severity)

    def test_convert_quality_to_severity_1(self):
        quality = 1
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(0, severity)

    def test_convert_quality_to_severity_2(self):
        quality = 2
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(0, severity)

    def test_convert_quality_to_severity_50(self):
        quality = 50
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(0, severity)

    def test_convert_quality_to_severity_300(self):
        quality = 300
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(0, severity)


    def test_convert_quality_to_severity_3(self):
        quality = 3
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(1, severity)

    def test_convert_quality_to_severity_100(self):
        quality = 100
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(1, severity)

    def test_convert_quality_to_severity_4(self):
        quality = 4
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(2, severity)

    def test_convert_quality_to_severity_200(self):
        quality = 200
        severity = FieldFetcher.ConvertQualityToSeverity(quality)
        self.assertEqual(2, severity)


