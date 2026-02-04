import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExercisesResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExercisesFixture:
    request = CreateExercisesRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)
