import httpx


login_payload = {
  "email": "dan12345@example.com",
  "password": "dan12345"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response: ", login_response_data)
print("Status code: ", login_response.status_code)


refresh_payload = {
  "refreshToken": login_response_data["token"]["refreshToken"]
}
refresh_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()
print("Refresh response: ", refresh_response_data)
print("Status code: ", refresh_response.status_code)