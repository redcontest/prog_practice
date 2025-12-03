from django.urls import path
from . import views  # Импортируем view-функции для указания в маршруте.


app_name = "dog_app"  # Чтобы использовать пространство имён.

urlpatterns = [
    path('', views.dogpage, name='dogpage'),
]
