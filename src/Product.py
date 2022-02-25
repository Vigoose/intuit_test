class Product(object):

    def __init__(self, product_name:str, description="") -> None:
        self.product_id = None
        self.product_name = product_name
        self.description = description

        print("created product {0.product_name}".format(self))

    def __str__(self) -> str:
        return "{0.product_id}: {0.product_name}".format(self)