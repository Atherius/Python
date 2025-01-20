import logging

class Logger:
    def __init__(self, log_file='speedpost.log'):
        self.logger = logging.getLogger('ApplicationLogger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self,message):
        self.logger.error(message)

    def log_warning(self,message):
        self.logger.warning(message)

    def log_critical(self,message):
        self.logger.critical(message)
        
    def log_info(self,message):
        self.logger.info(message)