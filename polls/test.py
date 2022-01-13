import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):
    def test_was_published_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

        # manage.py test polls는 polls 애플리케이션에서 테스트를 찾습니다.
        # django.test.TestCase 클래스의 서브 클래스를 찾았습니다.
        # 테스트 목적으로 특별한 데이터베이스를 만들었습니다.
        # 테스트 메소드 - 이름이 test로 시작하는 것들을 찾습니다.
        # test_was_published_recently_with_future_question에서 pub_date필드가 30일 미래인 Question 인스턴스를 생성했습니다
        #  … assertIs() 메소드를 사용하여, 우리가 False가 반환되기를 원함에도 불구하고 was_published_recently() 가 True를 반환한다는 것을 발견했습니다.
        # 테스트는 어떤 테스트가 실패했는지와 실패가 발생한 행까지 알려줍니다.
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        # assertIs = a is b
