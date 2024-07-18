from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.todo_list, name='todo_list'),
    path('create/', views.create_todo, name='create_todo'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
]