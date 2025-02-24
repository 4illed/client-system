from client import Client
from user import User


class Admin(Client):
    def get_info(self): ...

    def manage_users(self, user, action, **kwargs):
        """
        Метод для управления пользователями.
        """
        if isinstance(user, User):
            if action == "change_username":
                user.update_info(name=kwargs.get("new_name"))
            elif action == "change_email":
                user.update_info(email=kwargs.get("new_email"))
            elif action == "delete_user":
                del user
            else:
                return "Действие не поддерживается"
        else:
            return "Неверный тип пользователя"
