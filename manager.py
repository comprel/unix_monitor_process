# coding:utf-8

import time
from check_register_process import check_register

if __name__ == '__main__':
    while True:
        check_register()
        time.sleep(60)
