from abc import ABC, abstractmethod


class Client(ABC):
    def __init__(self, name, email):
        """Инициализация клиента с именем и адресом электронной почты."""
        self.name = name
        self.email = email

    def get_info(self):
        """Возвращает информацию о клиенте: имя и e-mail."""
        return f"Имя: {self.name}, Email: {self.email}"

    def update_info(self, name=None, email=None):
        """Обновляет данные клиента."""
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @abstractmethod
    def __str__(self):
        """
        Магический метод для красивого представления клиента.
        """
        from user import User
        from admin import Admin

        if isinstance(self, User):
            return f"Пользователь {self.name}"
        elif isinstance(self, Admin):
            return f"Администратор {self.name}"
        else:
            return f"Клиент {self.name}"
