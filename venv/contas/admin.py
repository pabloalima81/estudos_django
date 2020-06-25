# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria
from .models import Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)