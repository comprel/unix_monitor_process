# coding=utf8

import logging
import logging.config
import logging.handlers
from conf import BASE_LOG, LOG_PATH, LOG_LEVEL

levelmap = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


def _setuplog(filename, keep=None):
    logfile = LOG_PATH + '%s.log' % filename
    if keep:
        handler = logging.handlers.RotatingFileHandler(filename=logfile, maxBytes=500 * 1024 * 1025, backupCount=2)
    else:
        handler = logging.handlers.TimedRotatingFileHandler(filename=logfile, when='midnight', backupCount=7)
    logging.getLogger(filename).setLevel(levelmap.get(LOG_LEVEL, logging.INFO))
    formatter = logging.Formatter("[%(asctime)s] [%(filename)s-Line %(lineno)d] %(message)s")
    handler.setFormatter(formatter)
    logging.getLogger(filename).addHandler(handler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    logging.getLogger(filename).addHandler(consoleHandler)


def get_logger(name=None, keep=True):
    if not name:
        name = BASE_LOG
    _setuplog(filename=name, keep=keep)
    return logging.getLogger(name)


logger = get_logger()
