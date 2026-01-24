from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

    # Сравнение объектов целиком. Мы могли бы сравнить объекты actual и expected целиком:
    #
    # assert actual == expected, "Ответ с ошибкой валидации не совпадает с ожидаемым"
    #
    #     Плюсы:
    #         Код лаконичный и простой.
    #     Минусы:
    #         Если тест упадет, в логах будет просто сообщение, что объекты не совпадают, без конкретных деталей.
    #         В отчетах (например, Allure) ошибка будет выглядеть громоздко, и будет сложно понять, какое именно поле
    #         отличается.
    # Пошаговая проверка полей (наш вариант). Мы сравниваем каждое поле отдельно, включая все элементы списка details.
    #     Плюсы:
    #         Легко понять, какое именно поле не совпало.
    #         Ошибка в логах и отчетах Allure будет более читабельной.
    #     Минусы:
    #         Нужно писать дополнительный код.
    #         Если первая ошибка окажется невалидной, тест сразу упадет, и остальные проверки не выполнятся.
    #     Однако последний минус не критичен, так как в любом случае нам придется разбираться, что пошло не так.
    #     Поэтому выбор в пользу читаемости и атомарности проверок — лучший вариант.





def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.details, expected.details, "details")