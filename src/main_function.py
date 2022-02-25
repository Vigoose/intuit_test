import logging
import datetime

from Customer import Customer
from Seller import Seller

LOGGER = logging.getLogger(__name__)


class MainApplication():
    @staticmethod
    def current_time():
        return datetime.datetime.utcnow()

    def __init__(self) -> None:
        entire_products_list = []

    def run(self) -> None:
        print("I am running!!!")
        # Create Customer account
        tim = Customer("tim", "test@gmail.com")
        # Create Seller account
        jef = Seller("jef", "test_jeff@gmail.com")
        # Seller begin to create the product
        jef.create_product("Sample product", "this is a sample product")

        # Added the product into the entire product list


        # Buyer random selected one or more products


        # Buyer paying for the product


        # Generated the order and details 

if __name__ == "__main__":
    try:
        LOGGER.info("start")
        print("Start!")
        MainApplication().run()

    except Exception as main_exc:
        LOGGER.error("Failed to run the main application as %s" % main_exc)
