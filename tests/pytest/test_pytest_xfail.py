import pytest



@pytest.mark.xfail(reason="Найден баг тест падает")
def test_with_bug():
    assert 1 == 2
@pytest.mark.xfail(reason="Баг исправлен , но на тесте маркировка xfail")
def test_without_bug():
    assert  1 == 1

@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_external_services_is_unavailable():
    assert 1 == 2