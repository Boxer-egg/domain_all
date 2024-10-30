"""
log
打开文件
"""

import time
import sys

from loguru import logger as loguru_logger


class Logger:
    def __init__(self):
        # 配置loguru
        loguru_logger.remove()
        loguru_logger.add(
            sys.stdout,#控制台输出
            level="DEBUG",
            format="{time:HH:mm:ss} {level: <6} {message}",
            backtrace=True,
            diagnose=True,
        )
        loguru_logger.add(
            "logs/dn_{time:HH:mm:ss}.log", #文件输出
            rotation= "1 day",
            level="INFO",
            format="{time:HH:mm:ss} {level} {message}",
            backtrace=True,
            diagnose=True,
        )

    def debug(self,message):
        loguru_logger.debug(message)

        
