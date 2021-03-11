# reference from https://github.com/minayu416/chest

import os
import sys
import logging

from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


main_running_path = sys.argv[0]
separate_dir = main_running_path.split("/")

# get path that program call this module
base_dir = '/'.join(separate_dir[0:-1])

filename = separate_dir[-1]
filename = filename.split(".")[0]


class Logger(object):
    """Logger, for logging system message, print out and saving in log file.
    Init Logger obj with customized args: log_format, log_file, file_suffix, file_count, level, when, interval.
    using `set_log` function for setting new Logger object, it will register new Logger into default __logger,
    using `logger` function for getting logger
    Args:
        log_format (:obj:`str`, optional): Log format, customize log format
        log_file (:obj:`str`, optional): The place where put log file and naming of log
        file_suffix (:obj:`str`, optional): Add suffix string to distinguished different log file
        file_count (:obj:`int`, optional): Backup count
        level (:obj:`str`, optional): Set log level to define which level at least need to record log
        when (:obj:`str`, optional): a rollover occurs to change log file
        interval (:obj:`int`, optional): Define a time interval when rollover log file.
    Examples:
        >>> log_format = "[%(asctime)s] [%(levelname)s] %(message)s"
        >>> log_file = "../log/"
        >>> set_log(Logger(log_format=log_format, log_file=log_file))
        >>> logger().debug("Hello Word!")
        [2020-08-12 13:55:17,069] [DEBUG] Hello World!
        ../log/test.log
    """

    def __init__(self, log_format=None, log_file=None, file_suffix='%Y-%m-%d',
                 file_count=30, level='DEBUG', when='midnight', interval=1):

        self.LOG_FORMAT = log_format
        # default: locating where program run (/log/)
        self.LOG_FILE = log_file
        self.LOG_FILE_SUFFIX = file_suffix
        self.LOG_FILE_COUNT = file_count
        self.LOG_LEVEL = level
        self.LOG_WHEN = when
        # a rollover occurs:
        # S - Seconds
        # M - Minutes
        # H - Hours
        # D - Days
        # midnight - roll over at midnight
        # W{0-6} - roll over on a certain day; 0 - Monday
        self.LOG_INTERVAL = interval

        if self.LOG_FORMAT is None:
            log_format = '[%(asctime)s] [%(process)d] [%(levelname)s] [%(module)s.%(lineno)d.%(funcName)s] ' \
                         '[%(threadName)s] %(message)s'
            self.LOG_FORMAT = log_format

        if self.LOG_FILE is None:
            file_name = f'{filename}.log'
            self.LOG_FILE = os.path.join(base_dir, 'log', file_name)

        # Set logger
        path = Path(os.path.dirname(self.LOG_FILE))
        if not (path.exists() and path.is_dir()):
            os.makedirs(path)
        logging.basicConfig(
            level=getattr(logging, self.LOG_LEVEL),
            format=self.LOG_FORMAT
        )
        self.logger = logging.getLogger()
        self.logger.addHandler(self.get_log_handler())

    def get_log_handler(self):
        file_handler = TimedRotatingFileHandler(self.LOG_FILE, when=self.LOG_WHEN,
                                                interval=self.LOG_INTERVAL,
                                                encoding='UTF-8', backupCount=self.LOG_FILE_COUNT)
        file_handler.suffix = self.LOG_FILE_SUFFIX
        file_formatter = logging.Formatter(self.LOG_FORMAT)
        file_handler.setFormatter(file_formatter)
        file_handler.level = getattr(logging, self.LOG_LEVEL)
        return file_handler


__logger = None


def logger():
    """ Get logger which has been init and using it
    Returns:
        Logger.logger:
    Examples:
        >>> logger().debug("Hello Word!")
        [2020-08-12 13:55:17,069] [32528] [DEBUG] [log.74.<module>] [MainThread] Hello World!
    """
    return __logger


def set_log(logger_obj):
    """Init logger setting by Logger object
    Args:
        logger_obj (Logger obj): init logger with Logger object
    Returns:
        None
    Examples:
        >>> set_log(Logger())
    """
    global __logger
    __logger = logger_obj.logger
