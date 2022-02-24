from User import User

class Seller(User):
    """Class for customer
    
    """
    def __init__(self, user_name: str, email_address: str) -> None:
        self._user_name = user_name
        self.email_address = email_address
        self._phone = None
        self.order_list = []
        self._address = None

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