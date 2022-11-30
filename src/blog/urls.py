"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from random import randrange
import random
from tkinter.tix import Tree
import bcrypt
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils import lorem_ipsum
from faker import Faker
from blog import settings

from posts.views import BlogHome
faker = Faker()
number_of_data_to_create = 5
number_of_user_to_create = 2
print('-----------------')
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR / "templates")
print('-----------------')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('posts.urls'))
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

