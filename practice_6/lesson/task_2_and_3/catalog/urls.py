from . import views  # Для указания адреса views-функций.
from django.urls import path  # Для указания url-маршрута.


app_name = 'catalog'  # Для использования пространства имён задаем имя.

# Указываем единственный маршрут для обращения к view-функции detail.
urlpatterns = [
    path('', views.detail, name='detail'),
]
