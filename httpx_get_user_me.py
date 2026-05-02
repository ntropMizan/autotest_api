import httpx


login_payload = {
    "email": "test@mail.ru",
    "password": "123456"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

access_token = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token}"}
access_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Users response:",access_response.json())
print("Status code:",access_response.status_code)