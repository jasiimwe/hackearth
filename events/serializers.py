from rest_framework import serializers
from .models import Events


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('user','event_name','event_description', 'event_media')