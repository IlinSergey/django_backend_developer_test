from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import BookList, BookDetail


urlpatterns = [
    path("books/", BookList.as_view()),
    path("books/<int:pk>/", BookDetail.as_view()),
    path('token/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
