import logging


class BeanFormatter(logging.Formatter):
    # grey = "\x1b[38;20m"
    blue = '\x1b[38;5;39m'
    green = "\x1b[33;20m"
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "-%(asctime)s-   (%(name)s: %(levelname)s) = %(message)s)"

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: green + format + reset,
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
        self.client_logger.addHandler(stdout_handler)

    def get_core_logger(self) -> logging.Logger:
        return self.core_logger

    def get_client_logger(self) -> logging.Logger:
        return self.client_logger


# ------ Macros ------
logger = Log()
# Core macros
BN_CORE_DEBUG = logger.get_core_logger().debug
BN_CORE_INFO = logger.get_core_logger().info
BN_CORE_WARNING = logger.get_core_logger().warning
BN_CORE_ERROR = logger.get_core_logger().error
BN_CORE_CRITICAL = logger.get_core_logger().critical

# Client macros
BN_DEBUG = logger.get_client_logger().debug
BN_INFO = logger.get_client_logger().info
BN_WARNING = logger.get_client_logger().warning
BN_ERROR = logger.get_client_logger().error
BN_CRITICAL = logger.get_client_logger().critical


__all__ = [
    "BN_CORE_DEBUG", "BN_CORE_INFO", "BN_CORE_WARNING", "BN_CORE_ERROR", "BN_CORE_CRITICAL",
    "BN_DEBUG", "BN_INFO", "BN_WARNING", "BN_ERROR", "BN_CRITICAL"
]
