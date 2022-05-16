# API для Yatube
## _Программный интерфейс социальной сети Yatube_


В сети Yatube вы можете рассказать о самых важных вещах, привлечь внимание других пользователей и найти ребят, которые также увлечены чем-то как и вы.


## Описание возможностей

- Создание публикаций с иллюстрациями
- Тематические сообщества
- Подписки на любимых авторов
- Комментарии к публикациям


## Технологии

Для работы проекта требуются следующие библиотеки:

- Django==2.2.16
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==8.3.1
- PyJWT==2.1.0
- requests==2.26.0

Все необходимые библиотеки вы можете установить через файл requirements.txt. Инструкции приведены ниже.

## Установка - Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AnnaGolushko/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация к API


Информация об эндпоинтах API Yatube приведена в документации, разработанной с применением [Redoc]: <https://github.com/Redocly/redoc>
После запуска проекта документация API будет доступна по URL:
```
http://127.0.0.1:8000/redoc/
```

#### Несколько примеров запросов и ответов API:

1 Получение списка существующих публикаций:
```
http://127.0.0.1:8000/api/v1/posts/
```
Пример ответа:
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-10-14T20:41:29.648Z",
        "image": "string",
        "group": 0
    }
]
}
```

2 Добавление нового комментария к публикации. Анонимные запросы запрещены:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Пример входных данных в формате JSON:
```
{
"text": "Комментарий"
}
```
Пример ответа:
```
{
"id": 0,
"author": "string",
"text": "Комментарий",
"created": "2019-08-24T14:15:22Z",
"post": 1
}
```

## Лицензия

MIT
