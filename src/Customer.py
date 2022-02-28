from User import User

class Customer(User):
    """Class for customer
    
    """
    def __init__(self, user_name: str, user_id: int, email_address: str) -> None:
        self._user_name = user_name
        self.user_id = user_id
        self.email_address = email_address
        self._phone = None
        self.account_balance = 0
        self.order_list = []
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
    
    def reload_balance(self, amount: int):
        if amount < 0:
            print("You have to reload a positive amount!")
        else:
            self.account_balance += amount
        
