from rest_framework import serializers

from catalog.models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.full_name")

    class Meta:
        model = Book
        fields = ["id", "title", "author", "description", "published"]
