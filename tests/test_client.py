import unittest
from client import Client


# Dummy concrete subclass for testing purposes
class DummyClient(Client):
    def __str__(self):
        # Возвращаем строку согласно шаблону "Клиент <имя>"
        return f"Клиент {self.name}"


class TestClientMethods(unittest.TestCase):
    def setUp(self):
        # Инициализация DummyClient для каждого теста
        self.client = DummyClient("Иван Иванов", "ivan@example.com")

    def test_get_info(self):
        # Тест метода get_info
        expected_info = "Имя: Иван Иванов, Email: ivan@example.com"
        self.assertEqual(self.client.get_info(), expected_info)

    def test_update_info(self):
        # Тест метода update_info: обновляем имя и e-mail
        self.client.update_info(name="Анна Петрова", email="anna@example.com")
        expected_info = "Имя: Анна Петрова, Email: anna@example.com"
        self.assertEqual(self.client.get_info(), expected_info)

    def test_str_representation(self):
        # Тест магического метода __str__
        self.assertEqual(str(self.client), "Клиент Иван Иванов")
        # После обновления имени проверяем снова
        self.client.update_info(name="Петр Петров")
        self.assertEqual(str(self.client), "Клиент Петр Петров")


if __name__ == "__main__":
    unittest.main()
