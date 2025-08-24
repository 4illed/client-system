import unittest
from user import User
from admin import Admin


class TestAdminFunction(unittest.TestCase):
    def setUp(self):
        # Создаем объект Admin для тестирования
        self.admin = Admin("Артём", "example@mail.ru")

    def test_get_info(self):
        # Ожидаемый результат
        expected_info = {
            "Администратор": "Артём",
            "Email": "example@mail.ru",
        }
        # Проверяем, что метод get_info возвращает правильный словарь
        self.assertEqual(self.admin.get_info(), expected_info)

    def test_manage_users(self):
        user = User("Иван", "ivan@example.com")
        result = self.admin.manage_users(
            user, "change_username", new_name="Иван Иванов"
        )
        self.assertEqual(user.name, "Иван Иванов")
