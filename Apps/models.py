from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Keyword(models.Model):
    text = models.CharField(max_length=200)
    
def Search(Self):
    self.save()