from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Event