from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# 관리 인덱스 페이지에 Question을 추가
