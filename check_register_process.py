# coding:utf-8

import os
from base.base import MgrService
from base.logger import logger
from base.unix_monitor import check_process_isalive


def read_pid_file(filepath):
    with open(filepath) as file:
        pid = file.read().strip("\n")
        pid = pid.strip()
        return pid


def check_register():
    register_files = MgrService.get_register_file()
    for file in register_files:
        _basename = os.path.basename(file)
        filename = _basename.split(".")[0]
        pid = read_pid_file(file)
        if not check_process_isalive(pid=pid):
            logger.info("process pid: %s is not exists, unregister")
            MgrService.callback(processinfo=filename, pid=pid)
            MgrService.unregister(file)

