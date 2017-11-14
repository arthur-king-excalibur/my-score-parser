import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s %(name)-6s | %(levelname)-5s | %(message)s'
)

formatter_2 = logging.Formatter(
    '%(asctime)s %(name)-6s|%(levelname)-5s|%(module)-5s|%(funcName)-5s|%(message)s'
)

console = logging.StreamHandler()
console.setFormatter(formatter_2)

filehandler = logging.FileHandler('logger.log')
filehandler.setLevel(logging.WARNING)
filehandler.setFormatter(formatter_2)

logger.addHandler(console)
logger.addHandler(filehandler)
