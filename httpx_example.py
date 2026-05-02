import httpx

# ===================== 1. БАЗОВЫЙ GET-ЗАПРОС =====================
# Что проверяем: простой GET, получение JSON, статус-код
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)  # 200
print(response.json())       # {userId: 1, id: 1, title: "...", completed: False}

# ===================== 2. POST С JSON (json=) =====================
# Что проверяем: отправка JSON-данных на сервер
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code)  # 201 Created
print(response.json())       # сервер вернёт созданный объект с новым id

# ===================== 3. POST С form-данными (data=) =====================
# Что проверяем: отправка данных в формате application/x-www-form-urlencoded
data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)  # 200
print(response.json())       # httpbin вернёт наши данные внутри поля 'form'

# ===================== 4. GET С КАСТОМНЫМИ ЗАГОЛОВКАМИ =====================
# Что проверяем: передача авторизации или любых кастомных заголовков
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)  # посмотрим, что ушло на сервер (включая Authorization)
print(response.json())           # httpbin вернёт заголовки в поле 'headers'

# ===================== 5. GET С ПАРАМЕТРАМИ URL (query params) =====================
# Что проверяем: фильтрация/пагинация через параметры в URL
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)              # .../todos?userId=1
print(response.json())           # вернутся только задачи с userId=1

# ===================== 6. ЗАГРУЗКА ФАЙЛА =====================
# Что проверяем: отправка файлов (multipart/form-data)
# Внимание: файл example.txt должен существовать в той же папке
files = {"files": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())           # httpbin покажет информацию о загруженном файле

# ===================== 7. ПЕРЕИСПОЛЬЗОВАНИЕ КЛИЕНТА (контекстный менеджер) =====================
# Что проверяем: несколько запросов через один клиент (переиспользуем connection pool)
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # задача с id=1
print(response2.json())  # задача с id=2

# ===================== 8. ПЕРЕИСПОЛЬЗОВАНИЕ КЛИЕНТА С ЗАГОЛОВКАМИ =====================
# Что проверяем: глобальные заголовки для всех запросов клиента
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())   # httpbin покажет, что заголовок Authorization был отправлен

# ===================== 9. ОБРАБОТКА HTTP ОШИБОК (4xx, 5xx) =====================
# Что проверяем: автоматическое выбрасывание исключения через raise_for_status()
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # выбросит HTTPStatusError для 404
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")  # 404 Not Found

# ===================== 10. ОБРАБОТКА ТАЙМАУТА =====================
# Что проверяем: сервер отвечает слишком долго (delay/5 = задержка 5 секунд)
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=1)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")  # сработает через ~1 секунду