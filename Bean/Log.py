import logging


class BeanFormatter(logging.Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    format = "-%(asctime)s- (%(name)s: %(levelname)s) = %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Log:
    core_logger: logging.Logger
    client_logger: logging.Logger

    def __init__(self) -> None:
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(BeanFormatter())

        self.core_logger = logging.getLogger("BEAN")
        self.core_logger.setLevel(logging.DEBUG)
        self.core_logger.addHandler(stdout_handler)

        self.client_logger = logging.getLogger("APP")
        self.client_logger.setLevel(logging.DEBUG)
        self.core_logger.addHandler(stdout_handler)

    def get_core_logger(self) -> logging.Logger:
        return self.core_logger

    def get_client_logger(self) -> logging.Logger:
        return self.client_logger
