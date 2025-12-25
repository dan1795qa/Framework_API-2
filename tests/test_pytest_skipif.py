import pytest

SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(SYSTEM_VERSION == "v1.3.0", reason="Тест не может быть запущен на версии v1.3.0")
def test_system_version_valid():
    pass


@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="Тест не может быть запущен на версии v1.2.0")
def test_system_version_invalid():
    pass
