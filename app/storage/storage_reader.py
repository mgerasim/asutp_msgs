import os
import traceback

from app.config.config_loader import ConfigLoader
from app.message.processing.message_processing import MessageProcessing


class StorageReader:
    @staticmethod
    def read():
        cfg = ConfigLoader.load()
        print(cfg['storage'])
        for root, dirs, files in os.walk(cfg['storage']):
            for file in files:
                file_name = os.path.join(root, file)
                try:
                    MessageProcessing.run(file_name)
                except Exception:
                    print(f"Файл не обработан: {file_name}")
                    print(traceback.format_exc())

