import logging


def get_logger_instance(name='') -> object:
   
   log = logging.getLogger(name)
   log.setLevel(level=logging.DEBUG)

   return  log 