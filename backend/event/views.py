from django.shortcuts import render
from .models import Event
from rest_framework import viewsets, permissions
from .serializers import EventSerializer


class EventViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
