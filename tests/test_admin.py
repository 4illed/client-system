import unittest
from admin import Admin


class TestAdminFunction(unittest.TestCase):
    def setUp(self):
        # Создаем объект Admin для тестирования
        self.admin = Admin("Артём", "example@mail.ru")

    def test_get_info(self):
        # Ожидаемый результат
        expected_info = {
            "Администратор": "Артём",
            "Электронная почта": "example@mail.ru",
        }
        # Проверяем, что метод get_info возвращает правильный словарь
        self.assertEqual(self.admin.get_info(), expected_info)


if __name__ == "__main__":
    unittest.main()
