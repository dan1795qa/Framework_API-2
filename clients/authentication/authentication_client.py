from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class LoginRequestDict(TypedDict):
    """Описание структуры запроса на аутентификацию."""
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """Описание структуры запроса для обновления токена."""
    refreshToken: str


class authenticationClient(APIClient):
    """Клиент для работы с /api/v1/authentication"""
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.
        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
