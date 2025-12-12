from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateResponseSchema


class PublicUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestSchema) -> CreateResponseSchema:
        response = self.create_user_api(request)
        return CreateResponseSchema.model_validate_json(response.text)


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
