from log import set_log, Logger

from main.process import MainExecutor


if __name__ == '__main__':
    set_log(Logger())
    executor = MainExecutor()
    executor.work()
