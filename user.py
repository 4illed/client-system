from client import Client


class User(Client):
    def get_info(self): ...

    def get_purchase_history(self): ...
