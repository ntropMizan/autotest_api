import pytest


@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


@pytest.fixture(scope='function')
def users_client(settings):
    print("[FUNCTION] Создаем API клиент на каждый автотест")

@pytest.fixture(scope='module')
def module():
    print("[MODULE] Создаем API клиент на каждый модуль(фаил)")

@pytest.fixture(scope='package')
def package():
    print("[PACKAGE] Создаем API клиент на каждый пакет(папку)")

@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] отправляем данные в сервис аналитики")

class TestUsrFlow:
    def test_user_can_login(self, settings, user, users_client, send_analytics_data):
        ...

    def test_user_can_create_course(self, settings, user, users_client, send_analytics_data):
        ...



class TestAccountFlow:
    def test_user_account(self, settings, user, users_client, send_analytics_data):
        ...


@pytest.fixture
def user_data() -> dict:
    print("Создаем пользователя до теста (setup)") # До теста
    yield {"username": "test_user", "email": "test@example.com"} # выполняем тест
    print("Удаляем пользователя после теста (teardown)") # после теста

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_user_username(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'test_user'