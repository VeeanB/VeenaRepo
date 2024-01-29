import inspect
import logging
class BaseClass:
    import pytest
    import logging

    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("Information statements ")
        logger.warning("Somthing is in Waring statement mode")
        logger.error("A major error has happened ")
        logger.critical("Critical issues")
        return logger


