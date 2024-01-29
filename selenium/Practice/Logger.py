import logging
loger=logging.getLogger()
logging.basicConfig(filename="test.log" ,format=" %(asctime) s%(levelname) s%(message)s",filemode="w")
loger.setLevel(logging.DEBUG)
logging.debug("This is debug")
logging.info("This is debug")
logging.warning("This is debug")
logging.critical("This is debug")
logging.error("This is debug")