from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Instructor