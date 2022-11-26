from rest_framework import serializers
from .models import Events


class EventSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = ('organization','event_id','event_name','event_description', 'event_media')