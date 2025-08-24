from client import Client


class User(Client):

    def __init__(self, name, email):
        super().__init__(name, email)

    def get_info(self): ...

    def get_purchase_history(self): ...
