import httpx
from tools.fakers import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data: ", create_user_response_data)
print(get_random_email())


login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data: ', login_response_data)


patch_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_user_response = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
                                   json=patch_user_payload, headers=update_user_headers)
update_user_response_data = update_user_response.json()
print("Update user data: ", update_user_response_data)
print("Update user status_code: ", update_user_response.status_code)