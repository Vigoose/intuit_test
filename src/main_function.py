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
        self.entire_products_list = []

    def run(self) -> None:
        print("I am running!!!")
        # Create Customer account
        user_name = input("Please input your username: ")
        user_email = input("Please input your email address: ")
        tim = Customer(user_name, user_email)
        # Create Seller account
        jef = Seller("jef", "test_jeff@gmail.com")
        # Seller begin to create the product
        product = jef.create_product("Sample product", "this is a sample product")
        product2 = jef.create_product("Sample product2", "this is a sample product2")

        # Added the product into the entire product list
        self.entire_products_list.append(product)
        self.entire_products_list.append(product2)
        print("here is the list of Product {0}".format(self.entire_products_list))

        choose_one = input("Which one do you want to buy, input numbers: ")
        print(choose_one)

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
