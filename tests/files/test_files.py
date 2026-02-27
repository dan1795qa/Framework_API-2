import allure
import pytest
from http import HTTPStatus

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_file_not_found_response, assert_create_file_with_empty_filename_response, \
    assert_create_file_with_empty_directory_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity
from config import settings


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.FILES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.FILES)
class TestFiles:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create file")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get file")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Create file with empty filename")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/qa.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Проверка, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Проверка, что ответ API соответствует ожидаемой валидационной ошибке
        assert_create_file_with_empty_filename_response(response_data)

        # Дополнительная проверка структуры JSON, чтобы убедиться, что схема валидационного ответа не изменилась
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Create file with empty directory")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file=settings.test_data.image_png_file
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Проверка, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Проверка, что ответ API соответствует ожидаемой валидационной ошибке
        assert_create_file_with_empty_directory_response(response_data)

        # Дополнительная проверка структуры JSON
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete file")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        # 1. Удаляем файл
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        # 2. Проверяем, что файл успешно удален (статус 200 OK)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # 3. Пытаемся получить удаленный файл
        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # 4. Проверяем, что сервер вернул 404 Not Found
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # 5. Проверяем, что в ответе содержится ошибка "File not found"
        assert_file_not_found_response(get_response_data)

        # 6. Проверяем, что ответ соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Get file with incorrect file id")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
