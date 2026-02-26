from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        event_hooks={"request": [curl_event_hook]}
    )
