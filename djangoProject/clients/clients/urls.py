

from django.contrib import admin
from django.urls import path
from .views import list_clients, test_function, special_case_2003, special_case, month_archive, hello


urlpatterns = [
    path('hello/<str:name>/', hello),
    path('articles/2003/', special_case_2003),
    path('articles/<int:year>/', special_case),
    path('articles/<int:year>/<int:month>/', month_archive),
    path('test/', test_function),
    path('admin/', admin.site.urls),
    path('clients/',list_clients),
]
