

from django.contrib import admin
from django.urls import path
from .views import list_clients

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/',list_clients),
]
