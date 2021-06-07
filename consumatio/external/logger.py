import logging


def get_logger_instance(name='') -> object:
   """
   Configures the logger for the backend and returns a instance
   :return: <object> Logger instance
   """
   log = logging.getLogger(name)
   log.setLevel(level=logging.DEBUG)

   return  log 