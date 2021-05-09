import logging


def get_logger_instance() -> object:
    """
    Configures the logger for the backend and returns a instance
    :return: <object> Logger instance
    """
    logging.basicConfig(level=logging.INFO & logging.DEBUG,
                        format='%(asctime)s : %(levelname)s : %(message)s')
    return logging.getLogger(__name__)
