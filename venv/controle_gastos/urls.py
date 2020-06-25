"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from contas.views import home, listagem, nova_transacao, update, delete

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', listagem, name='url_listagem'),
    url('nova/', nova_transacao, name='url_nova'),
    url('update/<int:pk>', update, name='url_update'),
    url('delete/<int:pk>', delete, name='url_delete'),
    url('home/', home)
]
