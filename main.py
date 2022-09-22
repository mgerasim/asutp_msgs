# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from app.core.models.base_model import conn
from app.models.data import Data
from app.models.event import Event
from app.models.file import File
from app.storage.storage_reader import StorageReader

if __name__ == '__main__':
    conn.connect()
    try:
        conn.create_tables([
            File,
            Event,
            Data
        ])
    except Exception as e:
        print(str(e))

    while True:
        StorageReader.read()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
