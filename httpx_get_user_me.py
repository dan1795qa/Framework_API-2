import httpx

login_payload = {
  "email": "dan12345@example.com",
  "password": "dan12345"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response: ", login_response_data)
print("Status code: ", login_response.status_code)


access_payload = {
  'accessToken': login_response_data["token"]["accessToken"]
}

headers = {"Authorization": f"Bearer {access_payload['accessToken']}"}
response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
response_data = response.json()
print("Response: ", response_data)
print("Status code: ", response.status_code)

print('----------')