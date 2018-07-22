from django.db import models
from django.utils import timezone
# Create your models here.
class good(models.Model):
    author = models.CharField(max_length=20)
    price = models.FloatField()
    introduce = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)