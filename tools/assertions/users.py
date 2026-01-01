from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что ответ на текущего пользователя соответствует ожидаемому.

    :param actual: Фактическое значение схемы.
    :param expected: Ожидаемое значение схемы.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'email')
    assert_equal(actual.email, expected.email, 'email')
    assert_equal(actual.last_name, expected.last_name, 'last_name')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')


def assert_get_user_response(get_user_response: GetUserResponseSchema,
                             create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что пользователь из get-ответа совпадает с пользователем из create-ответа.
    """
    # Берём объекты UserSchema из ответов
    actual_user = get_user_response.user
    expected_user = create_user_response.user

    assert_user(actual_user, expected_user)
