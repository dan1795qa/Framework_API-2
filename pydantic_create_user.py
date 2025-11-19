from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Модель данных пользователя"""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Запрос на создание пользователя"""
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Ответ с данными созданного пользователя"""
    user: UserSchema
