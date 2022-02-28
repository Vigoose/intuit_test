
class Product(object):

    def __init__(self, product_name:str, global_id, price, description="") -> None:
        self.product_id = global_id
        self.product_name = product_name
        self.description = description
        self.price = price

        print("created product {0.product_name}".format(self))

    def __str__(self) -> str:
        return "{0.product_id}: {0.product_name}, ${0.price}".format(self)