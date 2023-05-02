import pytest
from django.urls import reverse

from catalog.models import Book


@pytest.mark.django_db
def test_take_book_list(api_client, user_token):
    """Тест на получение списка книг и отказ в доступе без токена"""
    url = "/api/books/"
    headers = {"Authorization": f"Token {user_token}"}
    response = api_client.get(path=url, headers=headers)
    assert response.status_code == 200
    response = api_client.get(path=url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_take_book(api_client, user_token, create_book):
    """Тест на получение информации о книге и отказ в доступе без токена"""
    url = f"/api/books/{create_book.id}/"
    headers = {"Authorization": f"Token {user_token}"}
    response = api_client.get(path=url, headers=headers)
    assert response.status_code == 200
    response = api_client.get(path=url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_book(api_client, user_token, create_book):
    """Тест на удаление книги и отказ в доступе без токена"""
    url = f"/api/books/{create_book.id}/"
    headers = {"Authorization": f"Token {user_token}"}
    response = api_client.delete(path=url, headers=headers)
    assert response.status_code == 204
    response = api_client.get(path=url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_book(api_client, user_token):
    """Тест на создание книги и отказ в доступе без токена"""
    url = "/api/books/"
    headers = {"Authorization": f"Token {user_token}"}
    data = {"title": "Test book"}
    response = api_client.post(path=url, headers=headers, data=data)
    assert response.status_code == 201
    book = Book.objects.first()
    assert book is not None
    response = api_client.get(path=url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_book2(api_client, user_token, create_book):
    headers = {"Authorization": f"Token {user_token}"}
    response = api_client.get(reverse("book_list"), headers=headers)

    assert response.status_code == 200
    assert len(response.data) == 1

    book_data = dict(response.data[0])
    print(book_data)
    assert book_data["title"] == create_book.title


@pytest.mark.django_db
def test_update_book(api_client, user_token, create_book):
    """Тест на обновление информации о книге и отказ в доступе без токена"""
    url = f"/api/books/{create_book.id}/"
    headers = {"Authorization": f"Token {user_token}"}
    payload = {
        "title": "Some Updated Title",
        "description": "It's simple description",
        "published": "2000-05-02"
    }
    response = api_client.put(url, headers=headers, data=payload, format="json")
    assert response.status_code == 200
    response = api_client.get(path=url)
    assert response.status_code == 401
