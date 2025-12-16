import httpx
from tools.fakers import fake

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data: ", create_user_response_data)


login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data: ', login_response_data)



create_file_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}


create_file_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open('testdata/files/qa.png', 'rb')},
    headers=create_file_header
)

create_file_response_json = create_file_response.json()
print("Create file data:", create_file_response_json)