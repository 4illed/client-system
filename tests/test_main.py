import unittest
from client import Client
from user import User
from admin import Admin


def check_client_type(client):
    """
    Проверяет тип объекта client.
    Использует isinstance для проверки, является ли объект экземпляром Client,
    и issubclass для проверки, является ли класс объекта подклассом Client.
    """
    is_instance = isinstance(client, Client)
    is_subclass = issubclass(type(client), Client)
    return is_instance, is_subclass

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client_instance = Client('Иван Иванов', 'ivan@example.com')
        self.user_instance = User("Иван Иванов", "ivan@example.com")
        self.admin_instance = Admin("Анна Петрова", "anna@example.com")
        
    def test_isinstance(self):
        is_instance, _ = check_client_type(self.client_instance)
        self.assertTrue(is_instance)
        
    def test_issubclass(self):
        _, is_subclass = check_client_type(self.client_instance)
        self.assertTrue(is_subclass)
        
    def test_isinstance_user(self):
        is_instance, _ = check_client_type(self.user_instance)
        self.assertTrue(is_instance)
        
    def test_issubclass_user(self):
        _, is_subclass = check_client_type(self.user_instance)
        self.assertTrue(is_subclass)
        
    def test_isinstance_admin(self):
        is_instance, _ = check_client_type(self.admin_instance)
        self.assertTrue(is_instance)
        
    def test_issubclass_admin(self):
        _, is_subclass = check_client_type(self.admin_instance)
        self.assertTrue(is_subclass)