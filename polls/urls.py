from django.urls import path

from . import views

# URL의 구분을 위해서 URLconf에 namespace를 추가해 준다.
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('/<int:question_id>/vote/', views.vote, name='vote'),
]

