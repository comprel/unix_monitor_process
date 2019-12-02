# coding: utf-8

import os
from conf import REGISTER_MONITOR_PATH
from logger import logger

register_path = REGISTER_MONITOR_PATH
if not os.path.exists(register_path):
    os.makedirs(register_path)


class MgrService(object):
    @classmethod
    def get_register_file(cls):
        pathDir = os.listdir(register_path)
        files = []
        for Dir in pathDir:
            if Dir.endswith(".pid"):
                files.append(os.path.join(register_path, Dir))
        return files

    @classmethod
    def unregister(cls, path):
        try:
            os.remove(path)
        except:
            pass

    @classmethod
    def callback(cls, processinfo, pid=None):
        logger.info("callback process")
        pass

    @classmethod
    def on_timeout(cls):
        pass

    @classmethod
    def monitor(cls):
        pass
