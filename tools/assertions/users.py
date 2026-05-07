from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema, UpdateUserRequestSchema, UpdateResponseSchema
from tools.assertions.base import assert_equal
import allure

from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Check create user response")

    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что фактические данные пользователя соответствует ожидаемому.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемие данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Check user")

    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.email, expected.email, 'email')
    assert_equal(actual.last_name, expected.last_name, 'last_name')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')


@allure.step("Check get user response")
def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные пользователя не совпадает.
    """
    logger.info(f"Check get user response")
    # Берём объекты UserSchema из ответов
    actual_user = get_user_response.user
    expected_user = create_user_response.user

    assert_user(actual_user, expected_user)


@allure.step("Check get user with incorrect user is response")
def assert_get_user_with_incorrect_user_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на получение пользователя с некорректным uuid соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info(f"Check get user with incorrect file is response")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",  # Тип ошибки, связанной с невалидным UUID.
                input="incorrect-user-id",  # Некорректный uuid.
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},
                # Минимальная длина строки должна быть 1 символ.
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                # Сообщение об ошибке.
                location=["path", "user_id"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check update user response")
def assert_update_user_response(request: UpdateUserRequestSchema, response: UpdateResponseSchema):
    """
    Проверяет, что ответ на обновление пользователя соответствует запросу.

    :param request: Исходный запрос на обновление пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Check update user response")

    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


@allure.step("Check user not found response")
def assert_user_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если пользователь не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info(f"Check user not found response")

    expected = InternalErrorResponseSchema(details="User not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check update user with incorrect email in body")
def assert_update_user_with_incorrect_email_in_body(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на обновление email пользователя на некорректный email соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info(f"Check update user with incorrect email in body")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="value_error",
                input="user12example.com",
                context={
                    "reason": "An email address must have an @-sign."},
                message="value is not a valid email address: An email address must have an @-sign.",
                location=["body", "email"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)
