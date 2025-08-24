import unittest
from client import Client
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Иван Иванов", "ivan@example.com")
    
    def test_get_info(self):
        expected_info = {
            "Пользователь": 'Иван Иванов', 
            "Email": 'ivan@example.com'
        }
        self.assertEqual(self.user.get_info(), expected_info)    
        
    def test_get_purchase_history_empty(self):
        self.assertEqual(self.user.get_purchase_history(), [])
    
    def test_add_purchase(self):
        self.user.add_to_purchase_history("Товар 1", 100)
        self.assertEqual(self.user.get_purchase_history(), [{"Товар": "Товар 1", "Цена": 100}])
        
    def test_purchase_history(self):
        self.user.add_to_purchase_history("Товар 1", 100)
        history = self.user.get_purchase_history()
        expected_history = [{"Товар": 'Товар 1', 'Цена': 100}]
        self.assertEqual(history, expected_history)
        