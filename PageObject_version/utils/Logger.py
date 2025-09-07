import logging


def get_logger(name):
    logger = logging.getLogger(name)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - Page:%(name)s - %(message)s")
    file1 = logging.FileHandler("PageObject_version/reports/Automation.log")
    logger.addHandler(file1)
    logger.setLevel(logging.INFO)
    file1.setFormatter(log_format)
    return logger
