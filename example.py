# coding:utf-8

import os
import time
import uuid
import random
import multiprocessing
from conf import REGISTER_MONITOR_PATH


def get_uuid():
    return uuid.uuid4()


def write_tmp_pid():
    pid = os.getpid()
    uuid = get_uuid()
    print "wirte_tmp_pid >>> %s.pid %s " % (uuid, pid)
    filepath = os.path.join(REGISTER_MONITOR_PATH, "%s.pid" % uuid)
    with open(filepath, 'w') as file:
        file.write("%s" % (pid))
        file.flush()


def write_random_pid():
    pid = random.randint(10000, 99999)
    uuid = get_uuid()
    print "wirte_random_pid >>> %s.pid %s " % (uuid, pid)
    filepath = os.path.join(REGISTER_MONITOR_PATH, "%s.pid" % uuid)
    with open(filepath, 'w') as file:
        file.write("%s" % (pid))
        file.flush()


def write_running_pid():
    pid = os.getpid()
    uuid = get_uuid()
    print "wirte_running_pid >>> %s.pid %s " % (uuid, pid)
    filepath = os.path.join(REGISTER_MONITOR_PATH, "%s.pid" % uuid)
    with open(filepath, 'w') as file:
        file.write("%s" % (pid))
        file.flush()

    while True:
        time.sleep(5)


if __name__ == '__main__':
    write_random_pid()
    wt = multiprocessing.Process(target=write_tmp_pid)
    wt.start()
    wt.join()
    write_running_pid()
