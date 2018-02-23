#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Written by Paulo Mariano
Github: https://github.com/paulomariano77
Email: paulomariano77@gmail.com

This class generates a log file
"""

import logging, os


class Logger(object):
    def __init__(self, message_type, msg, env_log_path=None):
        self.env_log_path = env_log_path
        self.message_type = message_type
        self.msg = msg


    def write(self):
        # creates logger object
        root_logger = logging.getLogger()
        log_formatter = logging.Formatter(fmt='[%(levelname)s] [%(asctime)s] %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
        root_logger.setLevel(logging.DEBUG)

        if os.environ.get(self.env_log_path) is not None:
            filename = os.environ.get(self.env_log_path)
        else:
            filename = 'daemon.log'

        # sends logs to file
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)
        
        # sends logs to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)
        
        # customize log message type
        if self.message_type == 'info':
            root_logger.info(self.msg)
        elif self.message_type == 'error':
            root_logger.error(self.msg)
        else:
            root_logger.debug(self.msg)
