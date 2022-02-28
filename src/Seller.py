from typing import List
from Product import Product
from User import User

class Seller(User):
    """Class for customer
    
    """
    def __init__(self, user_name: str, user_id: int, email_address: str) -> None:
        self._user_name = user_name
        self.email_address = email_address
        self._phone = None
        self.user_id = user_id
        self.order_list = []
        self.product_list: List[Product] = []
        self._address = None
        print('Created Customer {0._user_name} with {0.email_address}'.format(self))

    @property
    def user_name(self):
        return self._user_name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def show_order_list(self):
        for order in self.order_list:
            print(order)

    def set_address(self, address):
        self._address = address

    def create_product(self, product_name: str, global_product_id, price, description=None):
        product = Product(product_name=product_name, global_id=global_product_id, price=price, description=description)
        self.product_list.append(product)
        print("Seller {0.user_name} just created a {1} product and now is alive!".format(self, product_name))
        return product
