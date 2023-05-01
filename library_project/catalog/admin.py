from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import Author, Book

admin.site.register([Author, Book])

TokenAdmin.raw_id_fields = ['user']
