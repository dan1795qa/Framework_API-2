import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())
print("----------")

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
# print(response.request.headers)
print(response.json())
print("----------")


data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
# print(response.request.headers)
# print(response.json())
print("----------")


headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.json())  # Заголовки включены в
print("----------")


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач
print("----------")


files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())  # Ответ с данными о загруженном файле
print("----------")


with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи
print("----------")


client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())  # Заголовки включены в ответ
client.close()
print("----------")


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
print("----------")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=1)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
print("----------")