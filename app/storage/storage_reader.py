import os

from app.config.config_loader import ConfigLoader
from app.message.processing.message_processing import MessageProcessing


class StorageReader:
    @staticmethod
    def read():
        cfg = ConfigLoader.load()
        for root, dirs, files in os.walk(cfg['storage']):
            for file in files:
                file_name = os.path.join(root, file)
                MessageProcessing.run(file_name)

