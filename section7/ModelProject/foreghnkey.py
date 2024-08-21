import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
from django.utils import timezone
import pytz

setup()

from ModelApp.models import Schools, Students, Prefectures

pf = ['東京', '大阪']
sc = ['東', '西', '北', '南']
st = ['太郎', '次郎', '三郎']

def insert_records():
    for pf_name in pf:
        prefecture = Prefectures(name=pf_name)
        print(prefecture)
        prefecture.save()
        for sc_name in sc:
            school = Schools(name = sc_name,
                             prefecture=prefecture)
            print(school)
            school.save()
            for st_name in st:
                student = Students(
                    name=st_name, age=17,
                    major='物理', school=school
                )
                print(student)
                student.save()
                
# insert_records()

def select_students():
    sts = Students.objects.all()
    for st in sts:
        print(st.id, st.name, st.school.id, st.school.name, st.school.prefecture.id, st.school.prefecture.name)
        
select_students()

# Prefectures.objects.filter(id=1).delete()