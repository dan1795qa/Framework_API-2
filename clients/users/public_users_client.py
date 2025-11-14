from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client


# Добавили описание структуры пользователя
class User(TypedDict):
    """Описание структуры пользователя."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """Описание структуры запроса на создание пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа создания пользователя
class CreateResponseDict(TypedDict):
    """Описание структуры ответа создания пользователя."""
    user: User


class PublicUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestDict) -> CreateUserRequestDict:
        response = self.create_user_api(request)
        return response.json()


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
