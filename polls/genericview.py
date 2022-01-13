# Listiew 와 DetailView 는 각 개체목록 표시  특정 개체 유형에 대한 세부 정보 페이지 표시 개념을 추상화 한다.

# 각 제네릭 뷰 어떤 모델이 적용될 것인지 알아야한다. 이것은 model 속성을 통해 제공된다.
# Detail 제네릭 뷰는 URL에서 기본적으로 제공되는 키값이 pk라고 기대하기 때문에 이번예시에서 Question_id를 pk로 변환하여 제공하였다.

# 기본적으로 Detailview <appname>/<modelname>_detail.html 템플릿을 사용한다.
# template_name 속성을 통해 같은 generic view 를 구분할 수 있다.