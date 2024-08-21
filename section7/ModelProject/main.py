# レコード

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()

from ModelApp.models import Person

p = Person(
    first_name = 'Taro',
    last_name = 'Yamamoto',
    birthday = '2000-01-01',
    email = 'mail@mail.com' ,
    salary = 100000,
    memo = 'memo',
    web_site = 'http://www.com',
    update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
)



# p.save()

# class create
"""
Person.objects.create(
    first_name = 'Jiro', last_name = 'Ito',
    email = 'bb@maail.com', salary = 200000,
    memo = 'classMethods', web_site = None,
    update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
)
"""

# get_or_create

obj, created = Person.objects.get_or_create(
    first_name = 'Jiro', last_name = 'Ito',
    email = 'bb@maail.com', salary = 200000,
    memo = 'classMethods', web_site = None,
    update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))   
)

print(obj)
print(created)