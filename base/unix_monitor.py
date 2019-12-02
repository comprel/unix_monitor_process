# coding:utf-8

import os


def check_process_isalive(pid):
    return os.path.exists("/proc/%s" % pid)
