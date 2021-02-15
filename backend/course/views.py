from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ( CourseSerializer, 
LessonSerializer, InstructorSerializer)
from .models import *

class CourseViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class InstructorViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
