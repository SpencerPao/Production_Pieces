"""Example execution for illustrating logger capabilities..."""
import logging
from utils.logger import SetUpLogging

# Init logger
SetUpLogging().setup_logging()


def main():
    logging.info("Hello viewers; Please make sure to like, subscribe, and comment")
    logging.info("If you made it this far, much love :)")


if __name__ == '__main__':
    main()
