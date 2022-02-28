global_product_id = 1
global_user_id = 1

class GLOBAL_ID(object):

    def __init__(self) -> None:
        global global_product_id
        global global_user_id
        self.global_user_id = global_user_id
        self.global_product_id = global_product_id
    
    def add_new_item(self):
        pass


class GLOBAL_PRODUCT_ID(GLOBAL_ID):

    def __init__(self) -> None:
        super.__init__()
    
    def add_new_item(self):
        self.global_product_id += 1


class GLOBAL_USER_ID(GLOBAL_ID):

    def __init__(self) -> None:
        super.__init__()
    
    def add_new_item(self):
        self.global_user_id += 1
