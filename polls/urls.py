from django.urls import path

from . import views

# URL의 구분을 위해서 URLconf에 namespace를 추가해 준다.
app_name = 'polls'
urlpatterns = [
    # 제네릭 뷰
    path('', views.IndexView.as_view(), name='index'),
    path('/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('/<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('/<int:question_id>/vote', views.vote, name='vote'),

    # path('', views.index, name='index'),
    # path('/<int:question_id>/', views.detail, name='detail'),
    # path('/<int:question_id>/results/', views.results, name='results'),
    # path('/<int:question_id>/vote/', views.vote, name='vote'),
]
