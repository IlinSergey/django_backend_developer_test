from catalog.models import Book, Author
from .serializers import BookSerializer, BookListSerializer

from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = Author.objects.get(user=self.request.user)
        serializer.save(author=author)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
