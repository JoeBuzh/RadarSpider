# -*- coding: utf-8 -*-
# Author: Joe-BU
# Date: 2019-12-15

import os
import sys
import time
import logging
import logging.handlers


def init_logger(logfile):
    dir_path = os.path.dirname(logfile)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    except Exception as e:
        raise e
        print("Init Logfile Error!")

    handler = logging.handlers.RotatingFileHandler(logfile,
                                                   maxBytes=30*1024*1024, 
                                                   backupCount=10,
                                                   encoding='utf-8')
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger_instance = logging.getLogger(logfile.split("/")[-1])
    logger_instance.addHandler(handler)
    logger_instance.setLevel(logging.INFO)

    return logger_instance