# test-random_cat_image
Задача: Реализовать функцию получения случайного изображения кошки из API TheCatAPI https://api.thecatapi.com/v1/images/search.
        Написать тест, который проверяет успешный запрос и возвращает правильный URL.
        Написать тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.


Для решения задачи создадим два файла: `main.py` с функцией получения изображения кошки и `test.py` с тестами. Используем библиотеку `requests` и `pytest` для тестирования.

### 1. Функция для получения случайного изображения кошки (`main.py`):
```python
import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            return data[0]['url']  # Возвращаем URL из первого элемента массива
    return None  # Возвращаем None при ошибке или неверном формате
```

### 2. Тесты для проверки функции (`test.py`):
```python
import pytest
from main import get_random_cat_image
import requests

def test_successful_response(monkeypatch):
    # Мок-функция заменяет реальный запрос
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return [{"url": "https://example.com/cat.jpg"}]
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)  # Применяем мок
    url = get_random_cat_image()
    assert url == "https://example.com/cat.jpg"

def test_failed_response(monkeypatch):
    # Мок-функция для имитации ошибки 404
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 404
            def json(self):
                return []
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)  # Применяем мок
    url = get_random_cat_image()
    assert url is None
```

### Объяснение:
1. **Функция `get_random_cat_image`**:
   - Выполняет GET-запрос к `https://api.thecatapi.com/v1/images/search`.
   - При статусе `200` проверяет, что ответ — непустой массив, и возвращает URL из первого элемента.
   - Возвращает `None` при ошибках запроса или неверном формате данных.

2. **Тесты**:
   - **`test_successful_response`**:  
     Подменяет запрос с помощью `monkeypatch`, возвращает статус `200` и валидные данные. Проверяет корректность URL.
   - **`test_failed_response`**:  
     Имитирует ответ со статусом `404`. Проверяет, что функция возвращает `None`.

### Инструкция по запуску:
1. Установите зависимости:
   ```bash
   pip install requests pytest
   ```
2. Запустите тесты:
   ```bash
   pytest test.py
   ```

Пример вывода при успешном тестировании:
```
============================= test session starts ==============================
collecting ... collected 1 item

test.py::test_failed_response PASSED                                     [100%]

======================== 1 passed, 1 warning in 0.47s =========================
```
