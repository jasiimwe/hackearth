
from django.db import models
from core.models import TimestampedModel
from organization.models import Organization

# Create your models here.
class Events(TimestampedModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(max_length=200)
    event_media = models.CharField(max_length=1000)
    amount_to_raise = models.CharField(max_length=100)
    

    def __str__(self):
        return self.event_name


