from django.urls import path
from . import views

urlpatterns = [
    path('tambah/<int:num1>/<int:num2>/', views.tambah, name='tambah'),
    path('kurang/<int:num1>/<int:num2>/', views.kurang, name='kurang'),
    path('kali/<int:num1>/<int:num2>/', views.kali, name='kali'),
    path('bagi/<int:num1>/<int:num2>/', views.bagi, name='bagi'),
]