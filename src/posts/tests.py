from datetime import datetime
from pickle import TRUE
from random import random, randrange,randint
import bcrypt
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import lorem_ipsum
from posts.models import BlogPost
from faker import Faker






# Create your tests here.
fake = Faker()
article_to_create = 5
user_to_create = 2

for i in range(user_to_create):
    model = User.objects.get_or_create(
        username= f"user{i+1}",
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        password= "useruser", 
        email=f"user{i+1}@web.com",
        is_superuser =  True if i==0 else False,
        is_staff =  True if i==0 else False,
        is_active = True,
    )


# author= randrange(1,user_to_create),
for i in range(article_to_create):
    model = BlogPost.objects.get_or_create(
        title = fake.sentence(nb_words=10),
        author = User.objects.get(id = randrange(1,user_to_create+1)),
        created_on = datetime.now(),
        published = randint(0,1),
        content = " ".join(lorem_ipsum.paragraphs(randrange(3,5),True)),
    )