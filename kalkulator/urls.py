from django.urls import path
from . import views

urlpatterns = [
    path('tambah/<int:num1>/<int:num2>', views.tambah),
]