import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()

from ModelApp.models import Person
from django.utils import timezone

person = Person.objects.get(id=1)
print(person)
person.birthday = '1995-12-21'
person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

persons = Person.objects.filter(first_name='Taro')
for p in persons:
    p.first_name = person.first_name.lower()
    p.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
    p.save()
    
Person.objects.filter(first_name='taro').update(first_name='matsumoto', update_at='2020-01-01')
