from client import Client
from user import User
from admin import Admin


def check_client_type(client):
    """
    Проверяет тип объекта client.
    Использует isinstance для проверки, является ли объект экземпляром Client,
    и issubclass для проверки, является ли класс объекта подклассом Client.
    """
    if isinstance(client, Client):
        print("Объект является экземпляром Client")
    else:
        print("Объект не является экземпляром Client")

    if issubclass(type(client), Client):
        print("Класс объекта является подклассом Client")
    else:
        print("Класс объекта не является подклассом Client")


def print_client_info(client):
    """
    Печатает информацию о клиенте.
    Если объект является экземпляром User, печатает информацию о пользователе.
    Если объект является экземпляром Admin, печатает информацию об администраторе.
    """
    if isinstance(client, User):
        print("Информация о пользователе:", client)
    elif isinstance(client, Admin):
        print("Информация об администраторе:", client)
    else:
        print("Неизвестный тип клиента:", client)


# Пример использования функций:
if __name__ == "__main__":
    # Создаем объекты, предполагая, что классы User и Admin реализуют необходимые методы
    user_instance = User("Иван Иванов", "ivan@example.com")
    admin_instance = Admin("Анна Петрова", "anna@example.com")

    print("== Проверка типа user_instance ==")
    check_client_type(user_instance)
    print_client_info(user_instance)

    print("\n== Проверка типа admin_instance ==")
    check_client_type(admin_instance)
    print_client_info(admin_instance)
