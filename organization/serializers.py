from pyexpat import model
from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('user','organization_name','organization_description','contact')
