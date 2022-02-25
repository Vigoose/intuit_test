class User(object):

    def __init__(self, user_name, user_email) -> None:
        self._user_name = user_name
        self._user_email = user_email
        self.user_id = 