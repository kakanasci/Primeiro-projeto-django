# polls/admin.py

from django.contrib import admin
from .models import Question, Choice

# Registra o modelo Question no painel de administração
admin.site.register(Question)

# Registra o modelo Choice no painel de administração
admin.site.register(Choice)
