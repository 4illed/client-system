from client import Client


class User(Client):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.purchase_history = []
        
    def get_info(self): 
        return {
            'Пользователь': self.name, 
            'Email': self.email,
        }
    
    def add_to_purchase_history(self, product_name, price):
        """Добавляет товар в историю покупок"""
        purchase = {
            'Товар': product_name,
            'Цена': price
        }
        self.purchase_history.append(purchase)
        
    def get_purchase_history(self):
        """История покупок"""
        return self.purchase_history
