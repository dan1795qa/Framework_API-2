from http import HTTPStatus
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
import allure
from allure_commons.types import Severity


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.USERS)
class TestUsers:
    @pytest.mark.parametrize("email", [
        "mail.ru",
        "gmail.com",
        "example.com"
    ])
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        # allure.dynamic.title(f"Create user: {email}")

        request = CreateUserRequestSchema(
            email=fake.email(domain=email)
        )

        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), response_data.model_json_schema())
