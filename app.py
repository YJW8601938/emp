import logging
import os
from logging import handlers
HEADRES={"Content-Type": "application/json"}
EMP_ID=""

def init_logging():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    sh=logging.StreamHandler()
    fh=logging.handlers.TimedRotatingFileHandler(os.path.dirname(os.path.abspath(__file__))+"/log/ihrm.log",
                                                 when="s",
                                                 interval=10,
                                                 backupCount=3,
                                                 encoding="utf-8")
    fmt="%(asctime)s %(levelname)s [%(name)s][%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s"
    formatter=logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)
if __name__ == '__main__':
    init_logging()
    logging.info("测试日志打印")