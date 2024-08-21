import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()

from ModelApp.models import Person

# 全て取得
# persons = Person.objects.all()

person = Person.objects.get(last_name = 'Yamamoto')
print(person, person.id)
