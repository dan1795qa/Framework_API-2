from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    # address: Address
    is_active: bool = Field(alias="isActive")


user_data = {
    'id': 1,
    "name": 'Alice',
    "email": "alice@example.com",
    "isActive": True
}
user1 = User(**user_data)
print(user1.model_dump())

# user2 = User(
#     id=1,
#     name="Alice",
#     email="alice@example.com",
#     address={"city": "Moscow", "zip_code": "11111"},  # либо   address=Address{city="Moscow", zip_code="11111"},
#     is_active=False
# )
#
# print(user2.model_dump())
# print(user2.model_dump_json())
