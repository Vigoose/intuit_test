import logging
import datetime

from Customer import Customer

LOGGER = logging.getLogger(__name__)


class MainApplication():
    @staticmethod
    def _current_time():
        return datetime.datetime.utcnow()

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("I am running!!!")
        time = Customer("tim", "test@gmail.com")
        print(time._user_name)

if __name__ == "__main__":
    try:
        LOGGER.info("start")
        print("Start!")
        MainApplication().run()

    except Exception as main_exc:
        LOGGER.error("Failed to run as %s" % main_exc)
