"""Portable Logger anywhere for import."""
import logging.config
import yaml
import os


class SetUpLogging():
    def __init__(self):
        self.default_config = os.path.join(os.path.dirname(
            os.path.abspath('__file__')), "Logging/config/logging_config.yaml")

    def setup_logging(self, default_level=logging.INFO):
        path = self.default_config
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                logging.captureWarnings(True)
        else:
            logging.basicConfig(level=default_level)
