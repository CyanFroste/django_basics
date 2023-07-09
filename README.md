### Init Project

```sh
django-admin startproject django_unchained
```

### Start Server

```sh
python manage.py runserver
```

### Create App

```sh
python manage.py startapp society
```

### Register App urls

Register the app (society) urls on `django_unchained/urls.py`

```py
urlpatterns = [
    path("", include("society.urls")),
    # others...
]
```

Register individual `view` urls on `society/urls.py`

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # others...
]
```

Corresponding views for the above urls on `society/views.py`

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at index.")

```

### Models

Register app on `django_unchained/settings.py`

```py
INSTALLED_APPS = [
    'society',
    # others...
]
```

Docs

- https://docs.djangoproject.com/en/4.2/topics/db/models/
- https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types

Create models on `society/models.py`

> Note - Classes should be written in [`PascalCase`](https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/)

```py
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # This user is a default model provided by django
    # for basic auth
    user: models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_created=True)
```

---

References

- https://www.youtube.com/watch?v=Mezody4yiXw&list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk
