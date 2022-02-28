import logging
import datetime
import traceback

from Customer import Customer
from Seller import Seller

GLOBAL_PRODUCT_ID = 0
GLOBAL_USER_ID = 0

LOGGER = logging.getLogger(__name__)


class MainApplication():
    @staticmethod
    def current_time():
        return datetime.datetime.utcnow()

    def __init__(self) -> None:
        self.entire_products_list = {}

    def run(self) -> None:
        global GLOBAL_PRODUCT_ID
        global GLOBAL_USER_ID
        print("I am running!!!")
        # Create Customer account
        print("Current time is {}".format(MainApplication.current_time()))
        user_name = input("Please input your username: ")
        user_email = input("Please input your email address: ")
        GLOBAL_USER_ID += 1
        buyer = Customer(user_name, GLOBAL_USER_ID, user_email)
        # Create Seller account
        GLOBAL_USER_ID += 1
        jef = Seller("jef",GLOBAL_USER_ID, "test_jeff@gmail.com")
        # Seller begin to create the product and add the product into the entire product list
        GLOBAL_PRODUCT_ID += 1
        product = jef.create_product("Sample product", GLOBAL_PRODUCT_ID, 100, description="this is a sample product")
        self.entire_products_list[GLOBAL_PRODUCT_ID] = product
        GLOBAL_PRODUCT_ID += 1
        product2 = jef.create_product("Sample product2", GLOBAL_PRODUCT_ID, 200, description="this is a sample product2")
        self.entire_products_list[GLOBAL_PRODUCT_ID] = product2

        print("here is the list of Product")
        print('*' * 12)
        for product_id in self.entire_products_list:
            print("{0}".format(self.entire_products_list[product_id]))

        choose_one = int(input("Which one do you want to browse, input numbers: "))
        print('*' * 12)
        print(self.entire_products_list[choose_one])
        ok_to_buy = input("Want to buy this item? Y/N: ")
        # Buyer random selected one or more products
        while ok_to_buy != "Y":
            print('*' * 12)
            for product_id in self.entire_products_list:
                print("{0}".format(self.entire_products_list[product_id]))
            choose_one = int(input("Which one do you want to browse, input numbers: "))
            print(self.entire_products_list[choose_one])
            print(self.entire_products_list[choose_one].description)
            ok_to_buy = input("Want to buy this item? Y/N: ")
        # Buyer paying for the product
        to_buy_product = self.entire_products_list[choose_one]
        while buyer.account_balance < to_buy_product.price:
            want_reload = input("You don't have enough money for this! Do you want to reload? Y/N: ")
            if want_reload == "Y":
                reload_amount = int(input("Please choose how much you want to reload: "))
                buyer.reload_balance(reload_amount)
        buyer.account_balance -= to_buy_product.price
        print(buyer.account_balance)

        # Generated the order and details 

if __name__ == "__main__":
    try:
        LOGGER.info("start")
        print("Start!")
        MainApplication().run()

    except Exception as main_exc:
        traceback.print_exc()
        LOGGER.error("Failed to run the main application as: %s" % main_exc)
