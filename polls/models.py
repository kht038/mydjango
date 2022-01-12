import datetime

from django.db import models
from django.utils import timezone

# __str__ 메소드는 django 가 자동으로 생성하는 관리사이트에서도 객체의 표현이 사용되기 때문
# 시간대 조작에 대해 더 잘 알고싶다면 https://docs.djangoproject.com/ko/4.0/topics/i18n/timezones/


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 질문
    pub_date = models.DateTimeField('date published')  # 발행일

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 선택 텍스트
    votes = models.IntegerField(default=0)  # 투표 집계

    def __str__(self):
        return self.choice_text


# 데이터베이스의 각 필드는 Field 클래스의 인스턴스로서 표현된다. CharField는 문자 필드를 표현하고,
# DataTimeField는 날짜와 시간의 필드를 표현한다(datetime).
# ForeignKey 를 사용한 관계설정
# 각각의 Choice가 하나의 Question에 관계된다는 것을 알려준다.
# 다 대 일, 다 대 다, 일 대 일
# 모든 일반 데이터베이스와 관계들을 지원한다.

# python manage.py makemigrations 를 통해 변경사항에 대한 마이그레이션 생성
# python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용 (git add, commit같음)
