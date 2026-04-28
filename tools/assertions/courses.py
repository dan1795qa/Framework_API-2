from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema, GetCourseResponseSchema, \
    DeleteCourseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")


@allure.step("Check update course response")
def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
   Проверяет, что ответ на обновление курса соответствует данным из запроса.

   :param request: Исходный запрос на обновление курса.
   :param response: Ответ API с обновленными данными курса.
   :raises AssertionError: Если хотя бы одно поле не совпадает.
   """
    logger.info(f"Check update course response")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Check course")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


@allure.step("Check get course response")
def assert_get_courses_response(
        get_course_response: GetCoursesResponseSchema,
        create_course_response: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    logger.info(f"Check get course response")

    assert_length(get_course_response.courses, create_course_response, "courses")

    for index, create_course_response in enumerate(create_course_response):
        assert_course(get_course_response.courses[index], create_course_response.course)


@allure.step("Check create course response")
def assert_create_course_response(
        request: CreateCourseRequestSchema,
        response: CreateCourseResponseSchema
):
    """
    Проверяет, что ответ на создание курса соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Check create course response")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

    assert_equal(request.preview_file_id, response.course.preview_file.id, "preview_file_id")
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, "created_by_user_id")


@allure.step("Check get course response")
def assert_get_course_response(
        get_course_response: GetCourseResponseSchema,
        create_course_response: CreateCourseResponseSchema
):
    """
    Проверяет, что ответ на получение курса соответствует ответу на его создание.

    :param get_course_response: Ответ API при запросе данных курса.
    :param create_course_response: Ответ API при создании курса.
    :raises AssertionError: Если данные курса не совпадают.
    """
    logger.info(f"Check get course response")

    assert_course(get_course_response.course, create_course_response.course)


@allure.step("Delete course response")
def assert_delete_course_response(
        response
        # response: str | DeleteCourseResponseSchema,
        # expected_message: str | None = None,
):
    """
    Проверяет, что ответ на удаление курса корректен.

    :param response: ответ API (строка или RootModel[str]).
    :param expected_message: ожидаемый текст сообщения (если None, проверка на непустую строку).
    :raises AssertionError: если сообщение не совпадает или пустое.
    """
    logger.info("Check delete course response")

    # Если RootModel или аналогичная обёртка
    # if hasattr(response, "__root__"):
    #     msg = str(response.__root__)
    # else:
    #     msg = str(response)
    #
    # # Если передали expected_message, проверяем точное совпадение
    # if expected_message is not None:
    #     assert_equal(msg, expected_message, "delete_message")
    #
    # # Если не передали — просто проверяем, что строка не пустая
    # else:
    #     assert_equal(msg != "", True, "delete_message should not be empty")

    assert "null" in response.text
