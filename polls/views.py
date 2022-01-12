#from django.template import loader # render shortcut이 있다면 굳이 필요없음
from django.http import HttpResponse,HttpResponseRedirect , Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# get_list_or_404() 라는 함수도 있다. Get() 대신 filter()를 사용한다.
# 리스트가 비어있을 경우 Http404를 발생시킨다.

from .models import Question, Choice
# view는 두가지 중 하나를 하도록 되어있다. 요청한 페이지의 HttpResponse 객체를 반환하거나, Http404같은 예외를 발생하게 해야한다.
# 데이터 베이스의 레코드 읽기, PDF 생성, XML 출력, ZIP 파일 생성든 내가 원하는 무엇이든 Python의 어떤 라이브러리도 사용 할 수 있다.
# render() gkatnsms Request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세번째 선택적 인수로 받습니다.
# 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.


def index(request):
    # return HttpResponse
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) 템플릿을 사용하지 않는 경우
    # template = loader.get_template('polls/index.html')

    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(output) 템플릿을 사용하지 않고 불러오기
    # return HttpResponse(template.render(context, request)) shortcut render를 사용하지않을때의 템플릿불러오기
    # context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값 (템플릿에서 사용하기 위해 전달)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # get_object_or_404()를 사용하지 않을때
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "You're looking at the result of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # 요부분 리버스 잘못 묶어서 헤멤 담부터는 이런일 없어야된다


    # return HttpResponse("You're voting on question %s." % question_id)

# requst.POST 는 키로 전송된 자료에 접근할 수 있도록 해준다. request.POST['choice'] 는 선택된 설문의 ID를 문자열로 반환한다.(항상 문자열)
# request.GET 도 제공하지만 POST 요청을 통해서만 자료룰 수정하기를 추천
# 만약 POST에 choice 가 없으면, request.POST['choice']는 KeyError가 일어난다. 위 코드는 error를 체크하고 에러메시지와 함께 설문조사폼을 다시
# 보여준다
# 응답이 올바르다면 HttpResponse가 아니라 리디렉션을 시킨다. (사용자가 재전송될 URL로)
# POST데이터를 성공적으로 처리한 후에는 항상 HttpResponseRedirect를 반환 하는것이 좋다. 일반적으로 좋은 웹 개발 관행이다.
# reverse() 함수는 view함수에서 URL을 하드코딩 하지 않도록 도와준다.
# 제어를 전달하기 원하는 뷰의 이름을, URL 패턴의 변수부분을 조합해서 해당 뷰를 가리킨다.
# 위의 경우에서는 reverse() 호출은 'polls/3/results/를 반환할 것이다. 3은 question.id의 값이다.
