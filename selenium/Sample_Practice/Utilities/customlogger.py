import logging

def logger():
    logging.basicConfig(filename=r"C:\Users\veenu\PycharmProjects\PythonClass\selenium\Sample_Practice\Log\test.log", filemode="a",
                        format="%(created)s %(asctime)s %(levelname)s %(message)s",
                        level=logging.INFO,
                        force=True)
    log = logging.getLogger()
    return logging


