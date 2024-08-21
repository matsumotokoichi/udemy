import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()

from ModelApp.models import Place, Restaurants

pl = [('motomachi', 'yokohama'), ('tsukiji', 'tokyo')]

re = ['r-A', 'r-B']

for p_name, p_address in pl:
    p = Place(name=p_name, address=p_address)
    p.save()
    for r_name in re:
       r = Restaurants(place=p, name=r_name)
       r.save()