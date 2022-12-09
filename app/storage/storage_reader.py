import os
import traceback

from app.config.config_loader import ConfigLoader
from app.helpers.current_file_name_list_helper import CurrentFileNameListHelper
from app.message.processing.message_processing import MessageProcessing


class StorageReader:
    @staticmethod
    def read():
        cfg = ConfigLoader.load()
        print(cfg['storage'])
        current_files = CurrentFileNameListHelper.load()

        storage = os.getenv('STORAGE', cfg['storage'])

        for root, dirs, files in os.walk(storage):
            for file in files:
                file_name = os.path.join(root, file)
                try:
                    if file_name not in current_files:
                        print(f"Файл не загружен: {file_name}")
                        MessageProcessing.run(file_name)
#                    else:
#                       print(f"Файл загружен: {file_name}")
                except Exception:
                    print(f"Файл не обработан: {file_name}")
                    print(traceback.format_exc())

#       print('Обработка завершена')

