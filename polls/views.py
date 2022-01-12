from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question
# view는 두가지 중 하나를 하도록 되어있다. 요청한 페이지의 HttpResponse 객체를 반환하거나, Http404같은 예외를 발생하게 해야한다.
# 데이터 베이스의 레코드 읽기, PDF 생성, XML 출력, ZIP 파일 생성든 내가 원하는 무엇이든 Python의 어떤 라이브러리도 사용 할 수 있다


def index(request):
    # return HttpResponse
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) 템플릿을 사용하지 않는 경우
    template = loader.get_template('polls/index.html')

    context = {'latest_question_list' : latest_question_list }
    # return HttpResponse(output) 템플릿을 사용하지 않고 불러오기
    # return HttpResponse(template.render(context, request)) shortcut render를 사용하지않을때의 템플릿불러오기
    # context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값 (템플릿에서 사용하기 위해 전달)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
