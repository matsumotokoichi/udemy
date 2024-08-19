from django.db import models
from django.utils import timezone
import pytz

class BaseMeta(models.Model):
    
    create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))
    update_at = models.DateTimeField()
    
    class Meta:
        abstract = True


class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01') # type: ignore
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    web_site = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        ordering = ['salary']