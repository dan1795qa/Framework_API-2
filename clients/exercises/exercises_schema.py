from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """Описание структуры задания."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на получение заданий."""
    exercises: list[ExerciseSchema]


class GetExercisesQuerySchema(BaseModel):
    """Описание структуры запроса на получение списка заданий."""
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class GetExerciseResponseSchema(BaseModel):
    """Описание структуры ответа на получение задания."""
    exercise: ExerciseSchema


class CreateExercisesRequestSchema(BaseModel):
    """Описание структуры запроса на создание задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class CreateExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на создание задания."""
    exercise: ExerciseSchema


class UpdateExercisesRequestSchema(BaseModel):
    """Описание структуры запроса на обновление задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExercisesResponseSchema(BaseModel):
    """Описание структуры ответа на обновление задания."""
    exercises: list[ExerciseSchema]


class DeleteExerciseResponseSchema(BaseModel):
    """Описание структуры ответа на удаление задания."""
    Response: str
