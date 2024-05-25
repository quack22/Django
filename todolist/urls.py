from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='todo-index'),
    path('add/', views.add, name='todo-add'),
    path('update/<int:todo_id>/', views.update, name='todo-update'),
    path('delete/<int:todo_id>/', views.delete, name='todo-delete'),
]