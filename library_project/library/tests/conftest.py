import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from catalog.models import Book, Author


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def user():
    user = User.objects.create_user(username="test", password="passtest")
    return user


@pytest.fixture()
def user_token(user):
    Token.objects.create(user=user)
    return user.auth_token.key


@pytest.fixture()
def create_book(user):
    record_author = Author.objects.first()

    payload = {
        "title": "Some Title",
        "author": record_author,
        "description": "It's simple description",
        "published": "2023-05-02"
    }
    record = Book.objects.create(**payload)
    return record
