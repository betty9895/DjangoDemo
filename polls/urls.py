from django.urls import path
from . import views

# 定義APP
app_name = 'polls'



# 設定路由
# url_patterns [
#   path(url path, router, name),
#   re_path (url path(正則式), 控制函式, name)
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]