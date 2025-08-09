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