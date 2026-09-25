# Заняття 38. Маршрутизація та представлення (Path, Views)

## Мета заняття

На цьому занятті ми навчимося будувати сторінки Django-застосунку: налаштовувати URL-маршрути, створювати представлення, передавати дані в шаблони та розуміти, як запит проходить через Django до відповіді користувачу.[^1]

Після заняття ви зможете:

- налаштовувати URL-маршрути в Django;
- використовувати `path()` та `include()`;
- пояснювати, що таке `HttpRequest` і `HttpResponse`;
- писати функціональні представлення;
- передавати контекст у шаблони через `render()`;
- розуміти роль middleware та обробників помилок.[^1]

***

## URL-маршрутизація

URL-маршрутизація визначає, яке представлення Django має виконати для конкретної адреси в браузері. Коли користувач відкриває сторінку, Django дивиться на URL і шукає відповідний маршрут.[^1]

Наприклад:

- `/` — головна сторінка;
- `/about/` — сторінка “Про нас”;
- `/contacts/` — сторінка контактів;
- `/posts/1/` — сторінка конкретного запису.

Маршрутизація — це міст між адресою сторінки та логікою, яка має спрацювати.

***

## `path()`

`path()` — це основний спосіб описати маршрут у Django. Він зв’язує URL із view-функцією або view-класом.[^1]

### Приклад

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```


### Що тут відбувається

- `""` означає головну сторінку;
- `"about/"` — сторінка `/about/`;
- `views.home` і `views.about` — функції, які обробляють запит;
- `name="home"` і `name="about"` — імена маршрутів, які зручно використовувати в шаблонах.


### Маршрут із параметром

```python
path("posts/<int:post_id>/", views.post_detail, name="post_detail")
```

Тут `post_id` передається у view як число.

### Різні типи параметрів

Django підтримує кілька типів параметрів:

- `<int:id>` — ціле число (1, 2, 3...)
- `<str:username>` — текстовий рядок (user123)
- `<slug:article>` — slug із дефісами (my-article)
- `<uuid:id>` — універсальний унікальний ідентифікатор

### Приклади маршрутів

```python
path("users/<str:username>/", views.user_profile, name="user_profile")
path("articles/<slug:article>/", views.article_detail, name="article_detail")
path("files/<uuid:file_id>/", views.download_file, name="download_file")
path("posts/<int:post_id>/", views.post_detail, name="post_detail")
```

У view ці параметри передаються як аргументи функції:

```python
def user_profile(request, username):
    return render(request, "profile.html", {"username": username})

def article_detail(request, article):
    return render(request, "article.html", {"slug": article})

def download_file(request, file_id):
    return render(request, "download.html", {"file_id": file_id})

def post_detail(request, post_id):
    return render(request, "post.html", {"post_id": post_id})
```

***

## `include()`

`include()` використовується для підключення маршрутів іншого файлу. Це допомагає розділити маршрутизацію за застосунками.[^1]

### Приклад основного `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
```


### Приклад `core/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

`include()` робить код чистішим і зручнішим для масштабування.

***

## Обробники помилок

Django має вбудовані обробники помилок, які спрацьовують, якщо сторінка не знайдена або сталася серверна помилка.[^1]

### Найвідоміші помилки

- `404` — сторінка не знайдена;
- `500` — внутрішня помилка сервера;
- `403` — доступ заборонено;
- `400` — неправильний запит.


### Кастомні сторінки помилок

Можна створити власні сторінки для помилок, щоб користувач бачив не стандартне повідомлення, а красиву сторінку у стилі сайту.

Наприклад, для `404`:

```python
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, "404.html", status=404)
```


***

## Middleware

Middleware — це проміжне програмне забезпечення, яке обробляє запит і відповідь між браузером і view. Воно працює як “прослойка” між користувачем і логікою застосунку.[^1]

### Що може робити middleware

- перевіряти авторизацію;
- додавати інформацію в request;
- обробляти сесію;
- логувати запити;
- змінювати response.


### Приклад логіки

1. Запит приходить у Django.
2. Middleware перевіряє його (наприклад, перевіряє авторизацію).
3. Потім запит потрапляє у view.
4. View формує відповідь.
5. Middleware може змінити response перед відправкою.

Middleware — важлива частина Django, бо саме тут працюють багато системних механізмів.

### Практичний приклад: логування запитів

Створимо власне middleware для логування усіх HTTP-запитів:

Файл `core/middleware.py`:

```python
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Логування інформації про запит ДО view
        logger.info(
            f"Запит: {request.method} {request.path} | "
            f"IP: {request.META.get('REMOTE_ADDR')}"
        )
        return None  # Продовжити обробку
    
    def process_response(self, request, response):
        # Логування інформації після view
        logger.info(
            f"Відповідь: {request.path} | "
            f"Статус: {response.status_code}"
        )
        return response  # Повернути відповідь
```

Додаємо middleware у `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.RequestLoggingMiddleware',  # ← Наше middleware
]
```

Тепер усі запити будуть залогування з інформацією про метод, шлях, IP-адресу та статус-код відповіді.

### Порядок виконання middleware

Middleware виконуються в порядку, вказаному в MIDDLEWARE. Запит проходить через них **зверху вниз**, а відповідь — **знизу вверх**.

Наочна схема:

```
Запит → Middleware 1 → Middleware 2 → Middleware 3 → View
Запит ← Middleware 1 ← Middleware 2 ← Middleware 3 ← View (Response)
```

***

## Представлення (Views)

View — це частина Django, яка приймає HTTP-запит і повертає HTTP-відповідь. У простому випадку view може бути звичайною функцією.[^1]

### Основна роль view

- отримати запит;
- виконати потрібну логіку;
- звернутися до бази даних або сформувати дані;
- повернути користувачу відповідь.

***

## `HttpRequest`

`HttpRequest` — це об’єкт, який Django створює для кожного запиту. У ньому міститься інформація про користувача, URL, метод запиту, заголовки, параметри та інші дані.[^1]

### Що можна знайти в `request`

- `request.method`
- `request.GET`
- `request.POST`
- `request.user`
- `request.path`
- `request.headers`


### Приклад

```python
def home(request):
    print(request.method)
    print(request.path)
    return HttpResponse("Hello")
```


***

## `HttpResponse`

`HttpResponse` — це об’єкт відповіді, який Django повертає браузеру. Через нього можна віддати текст, HTML або інший вміст.[^1]

### Приклад

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```


### HTML-відповідь

```python
def home(request):
    return HttpResponse("<h1>Hello, Django!</h1>")
```

У реальних проєктах частіше використовують `render()`, а не чистий `HttpResponse` з HTML.

***

## Функціональні представлення

Функціональне представлення — це view, написане як звичайна функція Python. Це найпростіший і найзрозуміліший спосіб почати працювати з views.[^1]

### Приклад

```python
from django.http import HttpResponse

def about(request):
    return HttpResponse("About page")
```


### Приклад із даними

```python
from django.http import HttpResponse

def hello_user(request):
    name = "Olena"
    return HttpResponse(f"Hello, {name}!")
```

Функціональні представлення особливо зручні для початку навчання і для простих сторінок.

***

## `render()`

`render()` — це зручна функція Django, яка поєднує створення `HttpResponse` і підставлення шаблону. Вона приймає request, назву шаблону і контекст.[^1]

### Синтаксис

```python
return render(request, "index.html", context)
```


### Приклад

```python
from django.shortcuts import render

def home(request):
    context = {
        "title": "Головна сторінка",
        "message": "Ласкаво просимо до Django!",
    }
    return render(request, "home.html", context)
```


### Шаблон `home.html`

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

`render()` — це основний спосіб показувати HTML-сторінки в Django.

***

## Структура папок для шаблонів

Шаблони повинні лежати в правильному місці, щоб Django їх знайшов.

### Варіант 1: Шаблони в папці застосунку (рекомендовано)

```
project/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/          ← папка для шаблонів
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contacts.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   └── apps.py
└── db.sqlite3
```

### Варіант 2: Загальна папка шаблонів

```
project/
├── manage.py
├── config/
├── core/
├── templates/              ← загальна папка
│   ├── core/
│   │   ├── home.html
│   │   └── about.html
│   └── accounts/
│       └── login.html
└── db.sqlite3
```

### Налаштування TEMPLATES у settings.py

Для другого варіанту потрібно змінити `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Загальна папка шаблонів
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Рекомендація:** почніть із варіанта 1 (шаблони в папці застосунку). Це простіше для маленьких проєктів.

***

## Практика: перша сторінка застосунку

У цій частині ми створимо кілька сторінок і навчимося передавати в них дані.

### Крок 1. Створити застосунок

```bash
python manage.py startapp core
```


### Крок 2. Додати застосунок у `settings.py`

```python
INSTALLED_APPS = [
    ...
    "core",
]
```


### Крок 2.5. Створити папку для шаблонів

```bash
mkdir -p core/templates
```

Тепер структура буде такою:

```
core/
├── templates/           ← нова папка
├── views.py
├── urls.py
├── models.py
└── apps.py
```

### Крок 3. Створити файл `core/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
]
```


### Крок 4. Підключити маршрути в головному `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
```


### Крок 5. Створити `views.py`

```python
from django.shortcuts import render

def home(request):
    context = {
        "title": "Головна",
        "text": "Це головна сторінка сайту.",
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "title": "Про нас",
        "text": "Це сторінка з інформацією про проєкт.",
    }
    return render(request, "about.html", context)

def contacts(request):
    context = {
        "title": "Контакти",
        "email": "info@example.com",
        "phone": "+380 50 123 45 67",
    }
    return render(request, "contacts.html", context)
```


***

## Передача даних у шаблони

Контекст — це словник, який view передає в template. За допомогою контексту можна показувати в шаблоні змінні, списки, дати, числа та інші дані.[^1]

### Приклад списку

```python
def products(request):
    context = {
        "title": "Товари",
        "products": ["Laptop", "Mouse", "Keyboard"],
    }
    return render(request, "products.html", context)
```


### Шаблон

```html
<h1>{{ title }}</h1>

<ul>
    {% for product in products %}
        <li>{{ product }}</li>
    {% endfor %}
</ul>
```

Так ви можете передавати дані зі view у HTML.

### Повний приклад HTML-шаблону

Файл `core/templates/products.html`:

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            padding: 10px;
            margin: 5px 0;
            background-color: #e9ecef;
            border-left: 4px solid #007bff;
        }
        li:hover {
            background-color: #dee2e6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        
        {% if products %}
            <ul>
                {% for product in products %}
                    <li>{{ product }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <p>Товари відсутні.</p>
        {% endif %}
    </div>
</body>
</html>
```

Цей шаблон показує:
- Правильну HTML-структуру (DOCTYPE, head, body)
- CSS-стилізацію
- Передачу даних через `{{ title }}`
- Цикл через `{% for %}`
- Умовний блок `{% if %}`

***

## Повний приклад сторінок

### `core/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {
        "title": "Головна",
        "message": "Вітаємо на сайті!"
    })

def about(request):
    return render(request, "about.html", {
        "title": "Про нас",
        "company": "Python Course"
    })

# View із параметром URL
def user_profile(request, username):
    users_data = {
        "john": {"email": "john@example.com", "role": "admin"},
        "jane": {"email": "jane@example.com", "role": "user"},
        "bob": {"email": "bob@example.com", "role": "moderator"},
    }
    
    # Перевіряємо, чи існує користувач
    user_info = users_data.get(username)
    if user_info is None:
        return HttpResponse(f"Користувач {username} не знайдений", status=404)
    
    context = {
        "username": username,
        "email": user_info["email"],
        "role": user_info["role"],
    }
    return render(request, "profile.html", context)

# View з деталями посту
def post_detail(request, post_id):
    posts = {
        1: {"title": "Перший пост", "content": "Це мій перший пост на блозі."},
        2: {"title": "Другий пост", "content": "Продовжую писати про Django."},
        3: {"title": "Третій пост", "content": "Views та URL-маршрути."},
    }
    
    post = posts.get(post_id)
    if post is None:
        return HttpResponse(f"Пост з ID {post_id} не знайдений", status=404)
    
    context = {
        "post_id": post_id,
        "title": post["title"],
        "content": post["content"],
    }
    return render(request, "post.html", context)
```


### `core/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("users/<str:username>/", views.user_profile, name="user_profile"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
]
```


### `core/templates/home.html`

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <nav>
        <ul>
            <li><a href="{% url 'home' %}">Головна</a></li>
            <li><a href="{% url 'about' %}">Про нас</a></li>
            <li><a href="{% url 'user_profile' username='john' %}">Профіль John</a></li>
        </ul>
    </nav>
</body>
</html>
```


### `core/templates/profile.html`

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Профіль {{ username }}</title>
</head>
<body>
    <h1>Профіль користувача: {{ username }}</h1>
    <p><strong>Email:</strong> {{ email }}</p>
    <p><strong>Роль:</strong> {{ role }}</p>
    <a href="{% url 'home' %}">Назад на головну</a>
</body>
</html>
```


### `core/templates/post.html`

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>Post ID: {{ post_id }}</p>
    <article>{{ content }}</article>
    <a href="{% url 'home' %}">Назад на головну</a>
</body>
</html>
```

**Важливо:** у шаблонах можна використовувати `{% url 'name' %}` для генерування посилань на основі імені маршруту. Це безпечніше, ніж жорсткодити адреси.


***

## Як проходить запит

Типовий ланцюжок у Django такий:

1. Користувач відкриває URL.
2. Django шукає відповідний маршрут у `urls.py`.
3. Маршрут викликає view.
4. View створює або отримує дані.
5. Дані передаються в шаблон через `render()`.
6. Користувач бачить HTML-сторінку.

Цей ланцюжок — основа всієї роботи Django-застосунку.

***

## Типові помилки та як їх виправити

### Помилка 1: Застосунок не в INSTALLED_APPS

❌ **Помилка:**

```
ModuleNotFoundError: No module named 'core.models'
```

✅ **Виправлення:**

Додайте застосунок у `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ← Додайте ваш застосунок
]
```

### Помилка 2: View не імпортовано в urls.py

❌ **Помилка:**

```python
urlpatterns = [
    path("", home, name="home"),  # NameError: name 'home' is not defined
]
```

✅ **Виправлення:**

```python
from . import views  # або from .views import home

urlpatterns = [
    path("", views.home, name="home"),
]
```

### Помилка 3: Шаблон не знайдений

❌ **Помилка:**

```
TemplateDoesNotExist: home.html
```

✅ **Виправлення:**

Переконайтеся, що:
1. Папка `templates/` існує в папці застосунку
2. Файл розташований правильно: `core/templates/home.html`
3. Ім'я файлу правильне в `render()`

```python
# Правильно:
return render(request, "home.html", context)

# Неправильно:
return render(request, "templates/home.html", context)
```

### Помилка 4: Неправильне передавання параметрів URL

❌ **Неправильно:**

```python
path("posts/<post_id>/", views.post_detail)  # post_id не типізований
```

✅ **Правильно:**

```python
path("posts/<int:post_id>/", views.post_detail)
```

### Помилка 5: View не приймає параметр

❌ **Неправильно:**

```python
path("users/<str:username>/", views.user_profile)

def user_profile(request):  # Забув username!
    return render(request, "profile.html")
```

✅ **Правильно:**

```python
def user_profile(request, username):
    return render(request, "profile.html", {"username": username})
```

### Помилка 6: Неправильні слеші в URL

❌ **Неправильно:**

```python
path("about", views.about)  # Забув завершуючий слеш
```

✅ **Правильно:**

```python
path("about/", views.about)
```

### Помилка 7: Забули TEMPLATES DIR у settings.py

Якщо шаблони в окремій папці `templates/`, додайте в `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← Додайте це
        'APP_DIRS': True,
        ...
    },
]
```

### Алгоритм пошуку помилки

1. Перевіріть маршрут у `urls.py` — чи вказує на правильний view?
2. Перевіріть імпорти — чи імпортовані views?
3. Перевіріть сам view — чи він приймає всі параметри?
4. Перевіріть шаблон — чи файл існує в правильній папці?
5. Запустіть сервер знову — інколи потрібен перезапуск
6. log — Django виводить деталізовану інформацію про помилку

Якщо виникла помилка, варто спочатку прочитати stack trace Django — він вказує, де саме сталася помилка.



## Підсумок

На цьому занятті ви навчилися будувати просту структуру Django-сторінок: налаштовувати маршрути, створювати views, передавати дані в шаблони та розуміти базовий шлях обробки HTTP-запиту.[^1]

Це основа для наступних тем: шаблони, форми, Django ORM і побудова повноцінного веб-застосунку.