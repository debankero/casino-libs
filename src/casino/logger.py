import logging
import os
import sys
from logging.handlers import RotatingFileHandler

# from . import config

loggers = {}
log_handlers = []


class LogConfig:
    LOG_FILE_PATH = None
    LOG_LEVEL = logging.INFO
    LOG_FILE_MAX_SIZE = 1 * 1024 ** 2
    LOG_FILE_BACKUP_COUNT = 5
    LOG_STD_STREAM = None
    LOG_FORMAT = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'


def init_logging(
    log_file_path=None,
    log_level=logging.INFO,
    log_file_max_size=1 * 1024 ** 2,
    log_level_libs=logging.ERROR,
    log_file_backup_count=10,
    log_std_stream=sys.stdout,
    log_format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
):
    print('===>>>', log_file_path)
    LogConfig.LOG_FILE_PATH = log_file_path
    LogConfig.LOG_LEVEL = log_level
    LogConfig.LOG_FILE_MAX_SIZE = log_file_max_size
    LogConfig.LOG_FILE_BACKUP_COUNT = log_file_backup_count
    LogConfig.LOG_STD_STREAM = log_std_stream
    LogConfig.LOG_FORMAT = log_format

    if log_file_path:
        try:
            os.makedirs(os.path.dirname(log_file_path))
        except PermissionError:
            print(
                f'Unable to init logging to file, insufficient '
                f'permissions for path "{log_file_path}"'
            )
            exit(1)
        except OSError:
            # directories already exist
            pass

    # Set log level for libraries
    loggers_ = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers_:
        logger.setLevel(log_level_libs)


def get_logger(name=None, log_level=None):
    if log_level is None:
        log_level = LogConfig.LOG_LEVEL

    if name in loggers.keys():
        log = loggers[name]
        log.setLevel(log_level)
        return loggers[name]
    else:
        log = logging.getLogger(name)
        loggers[name] = log
        lh = []
        try:
            handler = RotatingFileHandler(
                LogConfig.LOG_FILE_PATH,
                'a',
                LogConfig.LOG_FILE_MAX_SIZE,
                LogConfig.LOG_FILE_BACKUP_COUNT,
                'utf-8'
            )

            lh.append(handler)
            log_handlers.append(handler)

        except PermissionError:
            print(
                f'Unable to init logging to file, insufficient '
                f'permissions for path "{LogConfig.LOG_FILE_PATH}"'
            )
            exit(1)
        except OSError as e:
            print(f'Unable to create RotatingFileHandler, error: {e}')

        if LogConfig.LOG_STD_STREAM:
            handler = logging.StreamHandler(LogConfig.LOG_STD_STREAM)
            lh.append(handler)
            log_handlers.append(handler)

        for handler in lh:
            handler.setLevel(log_level)
            handler.setFormatter(logging.Formatter(LogConfig.LOG_FORMAT))
            log.addHandler(handler)
            log.setLevel(log_level)

        log.debug(f'Logging initialized (name={name})')

        return log


def destroy():
    for handler in log_handlers:
        handler.close()
