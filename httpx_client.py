import httpx

login_payload = {
  "email": 'dan12345@example.com',
  "password": 'dan12345'
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data: ', login_response_data)

client = httpx.Client(
    base_url="http://127.0.0.1:8000",
    timeout=2,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print("Get user me data: ", get_user_me_response_data)