from operator import mod
from django.db import models
from core.models import TimestampedModel

# Create your models here.
class Events(TimestampedModel):
    user = models.ForeignKey('authenticate.User', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(max_length=200)
    event_media = models.URLField()
    
