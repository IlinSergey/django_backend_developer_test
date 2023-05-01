from django.urls import path, include

from .views import index


urlpatterns = [
    path("", index, name="index"),
    path('api-auth/', include('rest_framework.urls'))
]
