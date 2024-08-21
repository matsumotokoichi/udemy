import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()
from ModelApp.models import Person

Person.objects.filter(first_name='matsumoto').delete()
Person.objects.all().delete()