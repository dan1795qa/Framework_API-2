from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import allure

from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    logger.info(f"Validation JSON schema")

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
