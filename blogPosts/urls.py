# blogPosts/urls.py
from django.urls import path
from blogPosts import views


app_name = 'blogPosts'
urlpatterns = [
    path('', views.index, name='index'), # 'localhost:8000/posts/'
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete', views.delete, name='delete'),
]