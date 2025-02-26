from client import Client


class User(Client):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.purchase_history = []
        
    def get_info(self): 
        return f'User: {self.name}, Email: {self.email}'

    def get_purchase_history(self):
        return self.purchase_history
