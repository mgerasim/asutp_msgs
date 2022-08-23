import csv
import sys
import tempfile

from openpyxl import load_workbook

class MessageProcessing:
    @staticmethod
    def run(file_name):
        wb = load_workbook(file_name)
        sheet = wb.active

        for row in sheet.rows:
            print(row[0].value)


