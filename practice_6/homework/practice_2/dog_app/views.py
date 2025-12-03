from django.shortcuts import render
from django.http import HttpRequest, HttpResponse  # Для аннотации типов
import requests  # Для обращения к Dog API

# Чтобы избежать ошибку 403
from django.views.decorators.csrf import csrf_exempt


# Декорируем, чтобы функция не требовала проверки CSRF
@csrf_exempt
def dogpage(request: HttpRequest) -> HttpResponse:
    """
    View-функция для рендеринга страницы dog_page.html, на которой будет
    размещён список всех пород собак. На этой странице можно ввести через
    запятую интересующие породы и получить их фото.

    Args:
        request (HttpRequest): Http-запрос.

    Returns:
        HttpResponse: Http-ответ клиенту.
    """
    # Обращаемся к API и получаем список всех пород собак.
    breeds_response = requests.get('https://dog.ceo/api/breeds/list/all')
    breeds_data: dict = breeds_response.json()
    breeds = list(breeds_data['message'].keys())

    # Если пользователь ввёл список собак и хочет получить их фото, обработаем
    # это.
    dog_images = list()
    selected_breeds = list()
    if request.method == 'POST':
        breeds_string = request.POST.get('breeds', '')
        print(breeds_string)
        # Из полученной строки готовим список введённых пользователем пород.
        # Учитываем, что пользователь мог не поставить пробел после запятой
        # или же оставить две запятые подряд.
        selected_breeds = [
            breed.strip() for breed in breeds_string.lower().split(',')
            if breed.strip()
        ]
        for breed in selected_breeds:
            img_response = requests.get(
                f'https://dog.ceo/api/breed/{breed}/images/random'
            )
            img_data: dict = img_response.json()
            if img_data['status'] == 'success':
                dog_images.append(img_data['message'])
            else:
                dog_images.append(None)

    # Готовим словарь контекста со списком пород, списком введённых собак и их
    # фотографиями.
    zipped_selected_dogs = zip(selected_breeds, dog_images)
    context = {
        'breeds': breeds,
        'selected_breeds': selected_breeds,
        'dog_images': dog_images,
        'zipped_selected_dogs': zipped_selected_dogs,
    }
    print(context)
    # Отправляем рендериться.
    template = 'dog_page.html'
    return render(request, template, context)
